from SVGElement import Square
from EntityLayoutManager import EntityLayoutManager
from FlowLayoutManager import FlowLayoutManager

class BoxLayoutManager(object):
	def __init__(self, width = 300, height = 300, rows = 3, cols = 3, spacing = 15):
		self.width = width
		self.height = height
		self.rows = rows
		self.cols = cols
		self.spacing = spacing
		self.box_size = self.boxSize()
		self.vertical_spacing = self.verticalSpacing(self.box_size)
		self.horizontal_spacing = self.horizontalSpacing(self.box_size)

	def boxSize(self):
		# width = hor_length * cols + spacing * (cols+1)
		hor_length = (self.width - self.spacing * (self.cols+1)) / self.cols

		# height = ver_length * rows + spacing * (rows+1)
		ver_length = (self.height - self.spacing * (self.rows+1)) / self.rows

		return min(hor_length, ver_length)

	def verticalSpacing(self, box_size):
		# height = box_size * rows + ver_spacing * (rows+1)
		return (self.height - box_size*self.rows) / (self.rows+1)

	def horizontalSpacing(self, box_size):
		# width = hor_length * cols + spacing * (cols+1)
		return (self.width - box_size*self.cols) / (self.cols+1)

	def layout(self, boxes):
		elements = []

		# Silent failure if there are more boxes than rows and columns in the drawing
		for i in range(0, min(len(boxes), self.rows * self.cols)):
			(x, y) = self.position(i)
			elements.append(Square('box', x, y, self.box_size))

			entity_layout_manager = EntityLayoutManager(boxes[i], x, y, self.box_size, self.box_size)
			(count, partial) = boxes[i].entityCount()
			elements.extend(entity_layout_manager.layout(count, partial))

			flow_layout_manager = FlowLayoutManager(x, y, self.box_size, self.box_size)
			elements.extend(flow_layout_manager.layout(boxes[i].placement))

		return elements

	def position(self, index):
		row = index / self.cols
		col = index % self.cols

		x = self.horizontal_spacing + col * (self.box_size + self.horizontal_spacing)
		y = self.vertical_spacing + row * (self.box_size + self.vertical_spacing)

		return (x,y)