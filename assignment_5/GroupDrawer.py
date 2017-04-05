from PageBuilder import PageBuilder, SVGBuilder
from Styler import Styler
from BoxLayoutManager import BoxLayoutManager
from math import sqrt, ceil

class GroupLayoutManager(object):
	def __init__(self, width, height, groups):
		self.width = width
		self.height = height
		self.groups = groups

		len_groups = len(groups)
		self.cols = int(ceil(sqrt(len_groups)))
		self.rows = int(ceil(len_groups / (1.0 * self.cols)))
		self.spacing = 10
		self.cell_width = width / self.cols - (self.spacing+1)
		self.cell_height = height / self.rows - (self.spacing+1)

	def layout(self):
		elements = []
		entity_sizes = {}

		for row in range(0, self.rows):
			for col in range(0, self.cols):
				index = row * self.cols + col

				if index < len(self.groups):
					group = self.groups[index]
					(x, y) = self.position(row, col)
					box_layout_manager = BoxLayoutManager(x, y, self.cell_width, self.cell_height, group.boxes, group.unit_name)
					(elems, entity_size) = box_layout_manager.layout()
					elements.extend(elems)
					entity_sizes[group.unit_name] = entity_size

		return (elements, entity_sizes)

	def position(self, row, col):
		x = self.spacing + col * (self.cell_width + self.spacing)
		y = self.spacing + row * (self.cell_height + self.spacing)

		return (x,y)

class GroupDrawer(object):
	def __init__(self, drawing_name, settings, groups):
		self.drawing_name = drawing_name
		self.width = settings.width
		self.height = settings.height
		self.layout_manager = GroupLayoutManager(self.width, self.height, groups)
		self.units = list(map(lambda g: g.unit_name, groups))

	def draw(self, images, backgrounds):
		(svg_elements, entity_sizes) = self.layout_manager.layout()
		svg_builder = SVGBuilder(self.width, self.height)
		drawing = PageBuilder().build(self.drawing_name, svg_builder.build(svg_elements, entity_sizes, images, backgrounds))
		self.save(drawing)

		Styler(self.units, self.width).save()

	def save(self, drawing):
		with open(self.drawing_name + '.html', 'w') as file: 
			for line in drawing:
				file.write(line)