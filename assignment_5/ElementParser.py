import parsimonious
from FileParser import FileParser
from ModelParser import ModelParser
from ComponentParser import ComponentParser
from ModelObjects import Element, Stock, ValueElement, Flow, Variable, Source, Sink
import re

class ElementParser(object):
	def __init__(self, modelPath):
		self.modelPath = modelPath

	def parse(self):
		file_sections = self.getFileSections(self.getFileStr())

		model_elements = []
		for section in file_sections:
			temp_model_elements = self.getModelElements(section['string'])
			model_docstring = '' 

			for entry in temp_model_elements:
				if entry['kind'] == 'entry':
					entry.update(self.getEquationComponents(entry['eqn']))

			model_elements.extend(temp_model_elements)

		return self.transform(model_elements)

	def transform(self, model_elements):
		(stocks, potential_flows) = self.findStocks(model_elements)
		variables = self.findVariables(model_elements, potential_flows)
		flows = self.findFlows(model_elements, potential_flows)

		(stock_elements, stock_mapping) = self.transformStocks(stocks)
		variable_elements = self.transformVariables(variables)
		flow_elements = self.transformFlows(stocks, flows, stock_mapping)

		elements = []
		elements.extend(stock_elements)
		elements.extend(variable_elements)
		elements.extend(flow_elements)

		return elements

	def transformStocks(self, stocks):
		elements = []
		stock_mapping = {}

		for stock in stocks:
			el = Stock(stock['real_name'], stock['unit'])
			elements.append(el)
			stock_mapping[stock['real_name']] = el

		return (elements, stock_mapping)

	def transformVariables(self, variables):
		elements = []
		registered_variables = []

		for variable in variables:
			name = variable['real_name']

			if name not in registered_variables:
				elements.append(Variable(name, variable['unit']))
				registered_variables.append(name)

		return elements

	def transformFlows(self, stocks, flows, stock_mapping):
		elements = []

		for flow in flows:
			src = Source('src')
			dst = Sink('dst')
			flow_name = flow['real_name']
			for stock in stocks:
				if '-'+flow_name in stock['eqn']:
					src = stock_mapping[stock['real_name']]
				elif flow_name in stock['eqn']:
					dst = stock_mapping[stock['real_name']]

			elements.append(Flow(flow_name, src.unit, src, dst))

		return elements

	def findStocks(self, model_elements):
		stocks = []
		potential_flows = []
		for element in model_elements:
			if 'INTEG' in element['eqn']:
				stocks.append(element)
				integ_index = element['eqn'].find("INTEG (") + 7
				comma_index = element['eqn'].find(",")
				potential_flows.append(element['eqn'][integ_index:comma_index])

		return (stocks, potential_flows)

	def findFlows(self, model_elements, potential_flows):
		flows = []
		for element in model_elements:
			found_flow = False
			for potential_flow in potential_flows:
				if found_flow == False and element['real_name'] in potential_flow:
					flows.append(element)
					found_flow = True
		
		return flows

	def findVariables(self, model_elements, potential_flows):
		variables = []
		for element in model_elements:
			found_flow = False
			for potential_flow in potential_flows:
				if found_flow == False and element['real_name'] in potential_flow:
					found_flow = True
				if found_flow == False and 'INTEG' not in element['eqn']:
					variables.append(element)

		return variables

	def getFileStr(self):
		with open(self.modelPath, 'r') as in_file:
			text = in_file.read()   

		return text.replace('\n', '')

	def getFileSections(self, file_str):
		file_structure_grammar = r"""
		file = encoding? (macro / main)+
		macro = ":MACRO:" _ name _ "(" _ (name _ ","? _)+ _ ":"? _ (name _ ","? _)* _ ")" ~r".+?(?=:END OF MACRO:)" ":END OF MACRO:"
		main = !":MACRO:" ~r".+(?!:MACRO:)"

		name = basic_id / escape_group
		basic_id = ~r"[a-zA-Z][a-zA-Z0-9_\s]*"

		# between quotes, either escaped quote or character that is not a quote
		escape_group = "\"" ( "\\\"" / ~r"[^\"]" )* "\""
		encoding = ~r"\{[^\}]*\}"

		_ = ~r"[\s\\]*"  # whitespace character
		"""  # the leading 'r' for 'raw' in this string is important for handling backslashes properly

		parser = parsimonious.Grammar(file_structure_grammar)
		tree = parser.parse(file_str)

		return FileParser(tree).entries

	def getModelElements(self, model_str):
		model_structure_grammar = r"""
		model = (entry / section)+ sketch?
		entry = element "~" element "~" element ("~" element)? "|"
		section = element "~" element "|"
		sketch = ~r".*"  #anything

		# Either an escape group, or a character that is not tilde or pipe
		element = (escape_group / ~r"[^~|]")*

		# between quotes, either escaped quote or character that is not a quote
		escape_group = "\"" ( "\\\"" / ~r"[^\"]" )* "\""
		"""
		parser = parsimonious.Grammar(model_structure_grammar)
		tree = parser.parse(model_str)
		#print(tree)

		return ModelParser(tree).entries

	def getEquationComponents(self, equation_str):
		component_structure_grammar = r"""
		entry = component / subscript_definition / lookup_definition
		component = name _ subscriptlist? _ "=" _ expression
		subscript_definition = name _ ":" _ subscript _ ("," _ subscript)*
		lookup_definition = name _ &"(" _ expression  # uses lookahead assertion to capture whole group

		name = basic_id / escape_group
		subscriptlist = '[' _ subscript _ ("," _ subscript)* _ ']'
		expression = ~r".*"  # expression could be anything, at this point.

		subscript = basic_id / escape_group

		basic_id = ~r"[a-zA-Z][a-zA-Z0-9_\s]*"
		escape_group = "\"" ( "\\\"" / ~r"[^\"]" )* "\""
		_ = ~r"[\s\\]*"  # whitespace character
		"""

		# replace any amount of whitespace  with a single space
		equation_str = equation_str.replace('\\t', ' ')
		equation_str = re.sub(r"\s+", ' ', equation_str)

		parser = parsimonious.Grammar(component_structure_grammar)
		tree = parser.parse(equation_str)

		parse_object = ComponentParser(tree)

		return {'real_name': parse_object.real_name,
			'subs': parse_object.subscripts,
			'expr': parse_object.expression,
			'kind': parse_object.kind}