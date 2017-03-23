def quotify(obj):
	return '\"' + str(obj) + '\"'

class Style(object):
	def __init__(self, fill = "", stroke = "", stroke_width = 1):
		self.fill = fill
		self.stroke = stroke
		self.stroke_width = stroke_width

	def asSVG(self):
		object_attributes = vars(self).copy()
		format_attribute = quotify(";".join([self.stringify(k,v) for k, v in object_attributes.iteritems()]))
		return "style={0}".format(format_attribute)

	def stringify(self, key, value):
		return str(key).replace("_", "-") + ":" + str(value)

class SVGElement(object):
	def __init__(self, name, style):
		self.name = name
		self.style = style

	def asSVG(self):
		object_attributes = vars(self).copy()
		object_attributes.pop('style')

		pre = ["<" + self.name]
		post = [self.style.asSVG() + "/>"]
		formatted_attributes = pre + map(lambda k: self.formatAttribute(k), object_attributes.viewkeys()) + post
		
		format_string = " ".join(formatted_attributes)
		format_attributes = {k: quotify(v) for k, v in object_attributes.iteritems()}
		
		return format_string.format(format_attributes)

	def formatAttribute(self, attribute):
		return str(attribute) + "={0[" + str(attribute) + "]}"

class Circle(SVGElement):
	def __init__(self, style, cx, cy, r):
		SVGElement.__init__(self, "circle", style)
		self.cx = cx
		self.cy = cy
		self.r = r

class Rectangle(SVGElement):
	def __init__(self, style, x, y, width, height):
		SVGElement.__init__(self, "rect", style)
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class Square(Rectangle):
	def __init__(self, style, x, y, length):
		Rectangle.__init__(self, style, x, y, length, length)
