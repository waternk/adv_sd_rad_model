import ModelObjects
from ElementParser import ElementParser

class ElementProvider(object):
	def __init__(self, model_path):
		self.model_path = model_path
		self.parser = ElementParser(model_path)

	def provide(self):
		elements = self.parser.parse()

		stocks = self.stocks(elements)
		flows = self.flows(elements)

		return (self.placements(stocks, flows), stocks, flows)

	def placements(self, stocks, flows):
		in_out_flows = self.inOutFlows(stocks, flows)

		if self.checkNumberOfFlows(in_out_flows):
			return self.placeFlowsSigns(in_out_flows)
		else:
			print("The model has one or more stocks with more than four in or out flows")

	def stocks(self, elements):
		stocks = []
		for elem in elements:
			if type(elem) == ModelObjects.Stock:
				stocks.append(elem)
		return stocks

	def flows(self, elements):
		flows = []
		for elem in elements:
			if type(elem) == ModelObjects.Flow:
				flows.append(elem)
		return flows

	def inOutFlows(self,stocks,flows):
		in_out_flows = {}
		
		for stock in stocks:
			inflows = []
			outflows = []
			in_and_out = []
			
			for flow in flows:
				if stock.name == flow.dst.name:
					inflows.append(flow)
				elif stock.name == flow.src.name:
					outflows.append(flow)
		
			in_and_out = [inflows,outflows]
			in_out_flows[stock] = in_and_out

		return in_out_flows

	def checkNumberOfFlows(self,in_out_flows):
		for key in in_out_flows:
			if len(in_out_flows[key][0]) + len(in_out_flows[key][1]) > 4:
				return False
		
		return True

	def placeFlowsSigns(self,in_out_flows):
		for key in in_out_flows:
			flow_place = {}
			flow_sign = {}
			
			for flow in in_out_flows[key][0]:
				if 'left' not in flow_place.keys():
					flow_place['left'] = flow
					flow_sign['left'] = 'in'
				elif 'up' not in flow_place.keys():
					flow_place['up'] = flow
					flow_sign['up'] = 'in'
				elif 'down' not in flow_place.keys():
					flow_place['down'] = flow
					flow_sign['down'] = 'in'
				elif 'right' not in flow_place.keys():
					flow_place['right'] = flow
					flow_sign['right'] = 'in'
		
			for flow in in_out_flows[key][1]:
				if 'right' not in flow_place.keys():
					flow_place['right'] = flow
					flow_sign['right'] = 'out'
				elif 'down' not in flow_place.keys():
					flow_place['down'] = flow
					flow_sign['down'] = 'out'
				elif 'up' not in flow_place.keys():
					flow_place['up'] = flow
					flow_sign['up'] = 'out'
				elif 'left' not in flow_place.keys():
					flow_place['left'] = flow
					flow_sign['left'] = 'out'

			in_out_flows[key].append(flow_place)
			in_out_flows[key].append(flow_sign)

		return in_out_flows