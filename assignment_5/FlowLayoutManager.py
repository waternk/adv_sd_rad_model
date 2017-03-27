import warnings
from SVGElement import Rectangle

class FlowWrapper(object):
	def __init__(self, flow, out):
		self.flow = flow
		self.out = out
		self.class_name = 'outflow' if self.out else 'inflow'

class FlowPlacement(object):
	def __init__(self, placement_data):
		in_flows = placement_data[0]
		out_flows = placement_data[1]
		flow_place = placement_data[2]
		flow_sign = placement_data[3]

		if 'left' in flow_place:
			self.left = FlowWrapper(flow_place['left'], flow_sign['left'] == 'out')
		if 'up' in flow_place:
			self.up = FlowWrapper(flow_place['up'], flow_sign['up'] == 'out')
		if 'right' in flow_place:
			self.right = FlowWrapper(flow_place['right'], flow_sign['right'] == 'out')
		if 'down' in flow_place:
			self.down = FlowWrapper(flow_place['down'], flow_sign['down'] == 'out')

class FlowLayoutManager(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def layout(self, box_name, placement):
		elements = []

		if 'left' in vars(placement):
			(x, y, w, h) = self.leftBox()
			flow_name = box_name + "_left"
			elements.append(Rectangle(flow_name, placement.left.class_name, x, y, w, h))

		if 'up' in vars(placement):
			(x, y, w, h) = self.upBox()
			flow_name = box_name + "_up"
			elements.append(Rectangle(flow_name, placement.up.class_name, x, y, w, h))

		if 'right' in vars(placement):
			(x, y, w, h) = self.rightBox()
			flow_name = box_name + "_right"
			elements.append(Rectangle(flow_name, placement.right.class_name, x, y, w, h))

		if 'down' in vars(placement):
			(x, y, w, h) = self.downBox()
			flow_name = box_name + "_down"
			elements.append(Rectangle(flow_name, placement.down.class_name, x, y, w, h))

		return elements

	def leftBox(self):
		return (self.x, self.y + self.height*0.4, 3, self.height*0.2)

	def upBox(self):
		return (self.x + self.width*0.4, self.y, self.width*0.2, 3)

	def rightBox(self):
		return (self.x + self.width - 3, self.y + self.height*0.4, 3, self.height*0.2)

	def downBox(self):
		return (self.x + self.width*0.4, self.y+self.height-3, self.width*0.2, 3)