from FlowLayoutManager import FlowPlacement
from BoxDrawer import Box

class StockGroup(object):
	def __init__(self, unit_name, stocks, run_data, settings):
		self.unit_name = unit_name
		self.stocks = stocks
		self.run_data = run_data
		self.rows = settings.ball_rows
		self.cols = settings.ball_cols

	def boxes(self, placements):
		ball_counts = self.ballCount()
		boxes = []
		for stock in self.stocks:
			placement = placements[stock]
			box = Box(stock.name, self.unit_name, ball_counts[stock.name], FlowPlacement(placement), self.rows, self.cols)

			if boxes:
				index = self.insertPosition(placement, box, boxes)
				boxes.insert(index, box)
			else:
				boxes.append(box)

		return boxes

	def insertPosition(self, placement, box, boxes):
		inflows = placement[0]
		outflows = placement[1]
		
		position = 0
		profit = 0
		for i in range(0, len(boxes)):
			box_name = boxes[i].name

			current_profit = 0
			for flow in inflows:
				if flow.src.name == box_name:
					current_profit += 1

			for flow in outflows:
				if flow.dst.name == box_name:
					current_profit += 1

			if current_profit > profit:
				position = i
				profit = current_profit

		return position

	def ballCount(self):
		totals = self.run_data.sum(axis=1)
		max_total = max(totals)
		max_balls = self.rows * self.cols
		one_ball = max_total / max_balls

		return self.run_data.divide(one_ball).applymap(self.condition)

	def condition(self, val):
		if val < 0.001:
			return 0.000
		if 0.001 <= val <= 1:
			return 0.500
		return round(val)