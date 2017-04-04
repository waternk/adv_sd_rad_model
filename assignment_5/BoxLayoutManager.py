from SVGElement import Square, Circle
from EntityLayoutManager import EntityLayoutManager
from FlowLayoutManager import FlowLayoutManager
from math import cos, sin, sqrt, radians, pi

class BoxLayoutManager(object):
	def __init__(self, x, y, width, height, boxes):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.boxes = boxes

		box_len = len(boxes)

		self.angle = radians(360 / box_len)
		self.angle_shift = pi / box_len
		self.box_size = self.boxSize(box_len)
		self.inner_radius = self.innerRadius(self.box_size)

	def boxSize(self, box_count):

		# min(width, height) = box_size / 2 + radius + radius + box_size / 2
		# min(width, height) = box_size + 2*radius 

		outer_radius = min(self.width, self.height) / 2

		if box_count == 1:
			return outer_radius * 0.45

		x0 = self.width/2 + outer_radius * cos(0)
		y0 = self.height/2 + outer_radius * sin(0)
		x1 = self.width/2 + outer_radius * cos(self.angle)
		y1 = self.height/2 + outer_radius * sin(self.angle)

		dx = x1 - x0
		dy = y1 - y0
		dist = sqrt(dx*dx + dy*dy)

		return int(dist * 0.45)

	def innerRadius(self, box_size):
		# outer_radius = box_size + 2*radius
		# (outer_radius - box_size) / 2 = radius

		return (min(self.width, self.height) - box_size) / 2

	def layout(self):
		elements = []

		elements.append(Circle('box_placement', 'background', self.x + self.width/2, self.y + self.height/2, self.inner_radius))

		entity_sizes = [0]

		# Silent failure if there are more boxes than rows and columns in the drawing
		for i in range(0, len(self.boxes)):
			box = self.boxes[i]
			(x, y) = self.position(i)
			elements.append(Square(box.name, 'box', x, y, self.box_size))

			entity_layout_manager = EntityLayoutManager(box, x, y, self.box_size, self.box_size)
			entity_sizes.append(entity_layout_manager.circle_radius)
			elements.extend(entity_layout_manager.layout())

			# Editted out the flows
			#flow_layout_manager = FlowLayoutManager(x, y, self.box_size, self.box_size)
			#elements.extend(flow_layout_manager.layout(box.name, box.placement))

		return (elements, max(entity_sizes) * 2)

	def position(self, index):
		angle = self.angle * index + self.angle_shift

		x = self.x + ((self.width/2 + self.inner_radius * cos(angle)) - self.box_size/2)
		y = self.y + ((self.height/2 + self.inner_radius * sin(angle)) - self.box_size/2)

		return (x,y)