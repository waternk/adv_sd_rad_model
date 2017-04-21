import pandas as pd

class Box(object):
	def __init__(self, name, unit_name, run_data, placement, rows, cols):
		self.name = "_".join(name.lower().split())
		self.unit_name = unit_name
		self.placement = placement
		self.rows = rows
		self.cols = cols
		self.run_data = pd.DataFrame(run_data)[name].values