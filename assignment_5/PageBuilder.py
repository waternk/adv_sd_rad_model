from SVGElement import quotify

class PageBuilder(object):
	def build(self, body):
		pre = ["<!DOCTYPE html>", "<html>", "<head>", 
			"<link rel=\"stylesheet\" href=\"style.css\"/>",
			"<script src=\"snap.svg-min.js\"></script>",
			"<script src=\"animation.js\"></script>"
			"<script src=\"run_data.js\"></script>"
			"</head>", "<body>"]
		post = ["</body>", "</html>"]

		return pre + body + post

class SVGBuilder(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def build(self, svg_elements):
		pre = ["<svg id=\"animation_svg\" width={0} height={1}>".format(quotify(self.width), quotify(self.height))]
		elements = map(lambda e: e.text(), svg_elements)
		post = ["</svg>"]

		return pre + elements + post