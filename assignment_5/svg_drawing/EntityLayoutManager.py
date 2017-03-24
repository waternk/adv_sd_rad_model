from SVGElement import Circle, PartialCircle

class EntityLayoutManager(object):
	def __init__(self, box, x, y, width, height, spacing = 5):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.spacing = spacing
		self.unit_name = box.unit_name
		self.rows = box.rows
		self.cols = box.cols
		self.circle_radius = self.circleRadius()
		self.vertical_spacing = self.verticalSpacing(self.circle_radius)
		self.horizontal_spacing = self.horizontalSpacing(self.circle_radius)

	def circleRadius(self):
		# width = hor_length * cols + spacing * (cols+1)
		hor_diameter = (self.width - self.spacing * (self.cols+1)) / self.cols

		# height = ver_length * rows + spacing * (rows+1)
		ver_diameter = (self.height - self.spacing * (self.rows+1)) / self.rows

		return min(hor_diameter, ver_diameter) / 2

	def verticalSpacing(self, circle_radius):
		# height = 2 * radius * rows + ver_spacing * (rows+1)
		return (self.height - 2*circle_radius*self.rows) / (self.rows+1)

	def horizontalSpacing(self, circle_radius):
		# width = 2 * radius * cols + spacing * (cols+1)
		return (self.width - 2*circle_radius*self.cols) / (self.cols+1)

	def layout(self, entity_count, partial):
		elements = []

		if partial:
			(x, y) = self.position(0)
			elements.append(PartialCircle(self.unit_name, x, y, self.circle_radius))
		else:
			# Silent failure if there are more boxes than rows and columns in the drawing
			for i in range(0, min(entity_count, self.rows * self.cols)):
				(x, y) = self.position(i)
				elements.append(Circle(self.unit_name, x, y, self.circle_radius))

		return elements

	def position(self, index):
		row = index / self.cols
		col = index % self.cols

		x = self.x + self.circle_radius + self.horizontal_spacing + col * (2*self.circle_radius + self.horizontal_spacing)
		y = self.y + self.circle_radius + self.vertical_spacing + row * (2*self.circle_radius + self.vertical_spacing)

		return (x,y)