from FlowLayoutManager import FlowPlacement
from BoxDrawer import Box

class StockGroup(object):
	def __init__(self, unit_name, stocks, run_data, rows, cols):
		self.unit_name = unit_name
		self.stocks = stocks
		self.run_data = run_data
		self.rows = rows
		self.cols = cols

	def boxes(self, placements):
		boxes = []
		ball_counts = self.ballCount()
		for stock in self.stocks:
			placement = FlowPlacement(placements[stock])
			boxes.append(Box(stock.name, self.unit_name, ball_counts[stock.name], placement, self.rows, self.cols))

		return boxes

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