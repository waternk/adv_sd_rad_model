import warnings
from SVGElement import Rectangle

class Flow(object):
	def __init__(self, out = False):
		self.out = out
		self.class_name = 'outflow' if self.out else 'inflow'

class FlowPlacement(object):
	def __init__(self, flows):
		for flow in flows:
			if flow.out:
				self.addOutFlow(flow)
			else:
				self.addInFlow(flow)

	def addOutFlow(self, flow):
		if not 'right' in vars(self):
			self.right = flow
		elif not 'down' in vars(self):
			self.down = flow
		elif not 'up' in vars(self):
			self.up = flow
		elif not 'left' in vars(self):
			self.left = flow

	def addInFlow(self, flow):
		if not 'left' in vars(self):
			self.left = flow
		elif not 'up' in vars(self):
			self.up = flow
		elif not 'down' in vars(self):
			self.down = flow
		elif not 'right' in vars(self):
			self.right = flow

class FlowLayoutManager(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def layout(self, placement):
		elements = []

		if 'left' in vars(placement):
			(x, y, w, h) = self.leftBox()
			elements.append(Rectangle(placement.left.class_name, x, y, w, h))

		if 'up' in vars(placement):
			(x, y, w, h) = self.upBox()
			elements.append(Rectangle(placement.up.class_name, x, y, w, h))

		if 'right' in vars(placement):
			(x, y, w, h) = self.rightBox()
			elements.append(Rectangle(placement.right.class_name, x, y, w, h))

		if 'down' in vars(placement):
			(x, y, w, h) = self.downBox()
			elements.append(Rectangle(placement.down.class_name, x, y, w, h))

		return elements

	def leftBox(self):
		return (self.x, self.y + self.height*0.4, 3, self.height*0.2)

	def upBox(self):
		return (self.x + self.width*0.4, self.y, self.width*0.2, 3)

	def rightBox(self):
		return (self.x + self.width - 3, self.y + self.height*0.4, 3, self.height*0.2)

	def downBox(self):
		return (self.x + self.width*0.4, self.y+self.height-3, self.width*0.2, 3)