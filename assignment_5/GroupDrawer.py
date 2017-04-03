from PageBuilder import PageBuilder, SVGBuilder
from BoxLayoutManager import BoxLayoutManager
from math import sqrt, ceil

class GroupLayoutManager(object):
	def __init__(self, width, height, groups):
		self.width = width
		self.height = height
		self.groups = groups

		len_groups = len(groups)
		self.cols = int(sqrt(len_groups))
		self.rows = int(ceil(len_groups / (1.0 * self.cols)))

	def layout(self):
		elements = []

		for i in range(0, len(self.groups)):
			group = self.groups[i]
			(x, y) = self.position(i)
			box_layout_manager = BoxLayoutManager(x, y, self.width, self.height, group.boxes)
			elements.extend(box_layout_manager.layout())

		return elements

	def position(self, index):
		x = 0
		y = 0

		return (x,y)

class GroupDrawer(object):
	def __init__(self, drawing_name, settings, groups):
		self.drawing_name = drawing_name
		self.width = settings.width
		self.height = settings.height
		self.layout_manager = GroupLayoutManager(self.width, self.height, groups)

	def draw(self):
		svg_elements = self.layout_manager.layout()
		svg_builder = SVGBuilder(self.width, self.height)
		drawing = PageBuilder().build(svg_builder.build(svg_elements))
		self.save(drawing)

	def save(self, drawing):
		with open(self.drawing_name + '.html', 'w') as file: 
			for line in drawing:
				file.write(line)