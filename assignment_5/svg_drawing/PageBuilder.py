from SVGElement import quotify, Circle, Rectangle, Style

class PageBuilder(object):
	def __init__(self, name, builder):
		self.name = name
		self.builder = builder

	def build(self):
		pre = ["<!DOCTYPE html>", "<html>", "<body>"]
		body = self.builder.build()
		post = ["</body>", "</html>"]

		lines = pre + body + post

		with open(self.name + '.html', 'w') as file: 
			for line in lines:
				file.write(line)

class SVGBuilder(object):
	def __init__(self, width, height, elements):
		self.width = width
		self.height = height
		self.elements = elements

	def build(self):
		pre = ["<svg width={0} height={1}>".format(quotify(self.width), quotify(self.height))]
		elements = map(lambda e: e.asSVG(), self.elements)
		post = ["</svg>"]

		return pre + elements + post

style = Style(fill = "rgba(0,0,0,0)", stroke = "rgb(0,0,0)", stroke_width=2)

elements = [
	Circle(style, 50, 50, 50),
	Rectangle(style, 100, 100, 100, 50)
]

PageBuilder("index", SVGBuilder(300, 300, elements)).build()