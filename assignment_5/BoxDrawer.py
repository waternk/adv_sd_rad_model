from PageBuilder import PageBuilder, SVGBuilder
from BoxLayoutManager import BoxLayoutManager

class Box(object):
	def __init__(self, name, unit_name, run_data, placement, rows, cols):
		self.name = name
		self.unit_name = unit_name
		self.placement = placement
		self.rows = rows
		self.cols = cols
		self.run_data = run_data

	def entityCount(self):
		count = self.run_data[0]
		return (int(count), (int(count) == 0 and count > 0))

class BoxDrawer(object):
	def __init__(self, drawing_name, width, height):
		self.drawing_name = drawing_name
		self.width = width
		self.height = height
		self.layout_manager = BoxLayoutManager(width, height)

	def draw(self, boxes):
		svg_elements = self.layout_manager.layout(boxes)
		svg_builder = SVGBuilder(self.width, self.height)
		drawing = PageBuilder().build(svg_builder.build(svg_elements))
		self.save(drawing)

	def save(self, drawing):
		with open(self.drawing_name + '.html', 'w') as file: 
			for line in drawing:
				file.write(line)