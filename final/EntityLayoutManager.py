from SVGElement import Circle

class EntityLayoutManager(object):
	def __init__(self, box, x, y, width, height, spacing = 5):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.spacing = spacing
		self.box = box
		self.circle_radius = self.circleRadius()
		self.vertical_spacing = self.verticalSpacing(self.circle_radius)
		self.horizontal_spacing = self.horizontalSpacing(self.circle_radius)

	def circleRadius(self):
		# width = hor_length * cols + spacing * (cols+1)
		hor_diameter = (self.width - self.spacing * (self.box.cols+1)) / self.box.cols

		# height = ver_length * rows + spacing * (rows+1)
		ver_diameter = (self.height - self.spacing * (self.box.rows+1)) / self.box.rows

		return min(hor_diameter, ver_diameter) / 2

	def verticalSpacing(self, circle_radius):
		# height = 2 * radius * rows + ver_spacing * (rows+1)
		return (self.height - 2*circle_radius*self.box.rows) / (self.box.rows+1)

	def horizontalSpacing(self, circle_radius):
		# width = 2 * radius * cols + spacing * (cols+1)
		return (self.width - 2*circle_radius*self.box.cols) / (self.box.cols+1)

	def layout(self):
		elements = []

		for row in range(0, self.box.rows):
			for col in range(0, self.box.cols):
				(x,y) = self.position(row, col)
				index = row * self.box.cols + col

				circle_name = self.box.name + "_" + str(index)

				elements.append(Circle(circle_name, self.box.unit_name, x, y, self.circle_radius))

		elements.append(self.addPartial())

		return elements

	def addPartial(self):
		(x,y) = self.position(0, 0)

		circle_name = self.box.name + "_partial"
		return Circle(circle_name, self.box.unit_name, x, y, self.circle_radius)

	def position(self, row, col):
		x = self.x + self.circle_radius + self.horizontal_spacing + col * (2*self.circle_radius + self.horizontal_spacing)
		y = self.y + self.circle_radius + self.vertical_spacing + row * (2*self.circle_radius + self.vertical_spacing)

		return (x,y)