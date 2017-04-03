import pandas as pd
import pysd
from StockGroup import StockGroup

class ModelRunner(object):
	def __init__(self, model_path):
		self.model_path = model_path

	def run(self, stocks, settings):
		PySD_model = pysd.read_vensim(self.model_path)

		groups = {}
		for stock in stocks:
			if stock.unit in groups:
				groups[stock.unit].append(stock)
			else:
				groups[stock.unit] = [stock]

		stock_names = map(lambda s: s.name, stocks)
		run_data = PySD_model.run(return_columns=stock_names)

		stock_groups = []
		for unit in groups:
			group = groups[unit]
			stock_names = list(map(lambda s: s.name, group))
			stock_group = StockGroup(unit, group, run_data[stock_names], settings)
			stock_groups.append(stock_group)

		return stock_groups