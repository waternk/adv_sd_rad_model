from PageBuilder import PageBuilder, SVGBuilder
from BoxLayoutManager import BoxLayoutManager
from FlowLayoutManager import FlowPlacement, Flow

class Box(object):
	def __init__(self, unit_name, placement, rows, cols):
		self.unit_name = unit_name
		self.placement = placement
		self.rows = rows
		self.cols = cols

	def entityCount(self):
		count = (self.rows * self.cols) / 2.0
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

placement = FlowPlacement([Flow(), Flow(), Flow(True), Flow(True), Flow()])
boxes = [Box('A',placement,1,1), Box('A',placement,4,4), 
	Box('A',placement,5,5), Box('B',placement,3,4), 
	Box('A',placement,2,2), Box('A',placement,3,3), 
	Box('B',placement,9,9)]

drawer = BoxDrawer('index', 750, 750)
drawer.draw(boxes)