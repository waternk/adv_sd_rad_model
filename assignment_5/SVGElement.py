def quotify(obj):
	return '\"' + str(obj) + '\"'

class SVGElement(object):
	def __init__(self, id_name, tag_name, class_name):
		self.id_name = id_name
		self.tag_name = tag_name
		self.class_name = class_name

	def text(self):
		object_attributes = vars(self)

		pre = ["<" + self.tag_name]
		post = ["/>"]
		# list(map(lambda k: self.formatAttribute(k), object_attributes.viewkeys()))
		tag_attributes = [self.formatAttribute(k) for k,v in object_attributes.items()]
		formatted_attributes = pre + tag_attributes + post
		
		format_string = " ".join(formatted_attributes)
		format_attributes = {k: quotify(v) for k, v in object_attributes.items()}
		
		return format_string.format(format_attributes)

	def formatAttribute(self, attribute):
		if attribute == 'tag_name':
			return ''
		elif attribute == 'class_name':
			return 'class={0[class_name]}'
		elif attribute == 'id_name':
			return 'id={0[id_name]}'
		else:	
			return str(attribute) + "={0[" + str(attribute) + "]}"

class Circle(SVGElement):
	def __init__(self, id_name, class_name, cx, cy, r):
		SVGElement.__init__(self, id_name, "circle", class_name)
		self.cx = cx
		self.cy = cy
		self.r = r

class Rectangle(SVGElement):
	def __init__(self, id_name, class_name, x, y, width, height):
		SVGElement.__init__(self, id_name, "rect", class_name)
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class Square(Rectangle):
	def __init__(self, id_name, class_name, x, y, length):
		Rectangle.__init__(self, id_name, class_name, x, y, length, length)
