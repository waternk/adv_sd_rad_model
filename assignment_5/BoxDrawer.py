import pandas as pd
from PageBuilder import PageBuilder, SVGBuilder
from BoxLayoutManager import BoxLayoutManager

class Box(object):
	def __init__(self, name, unit_name, run_data, placement, rows, cols):
		self.name = "_".join(name.lower().split())
		self.unit_name = unit_name
		self.placement = placement
		self.rows = rows
		self.cols = cols
		self.run_data = pd.DataFrame(run_data)[name].values

class BoxDrawer(object):
	def __init__(self, drawing_name, settings, boxes):
		self.drawing_name = drawing_name
		self.width = settings.width
		self.height = settings.height
		self.layout_manager = BoxLayoutManager(self.width, self.height, boxes)

	def draw(self):
		svg_elements = self.layout_manager.layout()
		svg_builder = SVGBuilder(self.width, self.height)
		drawing = PageBuilder().build(svg_builder.build(svg_elements))
		self.save(drawing)

	def save(self, drawing):
		with open(self.drawing_name + '.html', 'w') as file: 
			for line in drawing:
				file.write(line)