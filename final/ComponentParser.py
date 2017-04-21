import parsimonious

class ComponentParser(parsimonious.NodeVisitor):
	def __init__(self, ast):
		self.subscripts = []
		self.real_name = None
		self.expression = None
		self.kind = None
		self.visit(ast)

	def visit_subscript_definition(self, n, vc):
		self.kind = 'subdef'

	def visit_lookup_definition(self, n, vc):
		self.kind = 'lookup'

	def visit_component(self, n, vc):
		self.kind = 'component'

	def visit_name(self, n, vc):
		(name,) = vc
		self.real_name = name.strip()

	def visit_subscript(self, n, vc):
		(subscript,) = vc
		self.subscripts.append(subscript.strip())

	def visit_expression(self, n, vc):
		self.expression = n.text.strip()

	def generic_visit(self, n, vc):
		return ''.join(filter(None, vc)) or n.text

	def visit__(self, n, vc):
		return ' '