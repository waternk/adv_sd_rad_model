def quotify(obj):
	return '\"' + str(obj) + '\"'

class SVGElement(object):
	def __init__(self, name, class_name):
		self.name = name
		self.class_name = class_name

	def text(self):
		object_attributes = vars(self)

		pre = ["<" + self.name]
		post = ["/>"]
		formatted_attributes = pre + map(lambda k: self.formatAttribute(k), object_attributes.viewkeys()) + post
		
		format_string = " ".join(formatted_attributes)
		format_attributes = {k: quotify(v) for k, v in object_attributes.iteritems()}
		
		return format_string.format(format_attributes)

	def formatAttribute(self, attribute):
		if attribute == 'class_name':
			return 'class={0[class_name]}'
		else:	
			return str(attribute) + "={0[" + str(attribute) + "]}"

class Circle(SVGElement):
	def __init__(self, class_name, cx, cy, r):
		SVGElement.__init__(self, "circle", class_name)
		self.cx = cx
		self.cy = cy
		self.r = r

class SemiCircle(SVGElement):
	def __init__(self, class_name, cx, cy, r):
		SVGElement.__init__(self, "path", class_name)
		self.d = "M{0},{1} a{2},{3} {4} {5},{6} {7},{8}".format(cx-r,cy,r,r,0,0,0,2*r,0)

class PartialCircle(Circle):
	def __init__(self, class_name, cx, cy, r):
		Circle.__init__(self, class_name, cx, cy, r)
		self.id = 'partial'

class Rectangle(SVGElement):
	def __init__(self, class_name, x, y, width, height):
		SVGElement.__init__(self, "rect", class_name)
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class Square(Rectangle):
	def __init__(self, class_name, x, y, length):
		Rectangle.__init__(self, class_name, x, y, length, length)
