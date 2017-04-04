from SVGElement import quotify

class PageBuilder(object):
	def build(self, body):
		pre = ["<!DOCTYPE html>", "<html>", "<head>", 
			"<link rel=\"stylesheet\" href=\"style.css\"/>",
			"<script src=\"snap.svg-min.js\"></script>",
			"<script src=\"animation.js\"></script>",
			"<script src=\"run_data.js\"></script>",
			"<script src=\"run_settings.js\"></script>",
			"</head>", "<body>"]
		post = ["</body>", "</html>"]

		return pre + body + post

class SVGBuilder(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def build(self, svg_elements, entity_sizes, images):
		pre = ["<svg id=\"animation_svg\" width={0} height={1}>".format(quotify(self.width), quotify(self.height))]
		patterns = self.buildPatterns(entity_sizes, images)
		elements = list(map(lambda e: e.text(), svg_elements))
		post = ["</svg>"]

		return pre + patterns + elements + post

	def buildPatterns(self, entity_sizes, images):
		pre = ["<defs>"]

		body = []
		for k,v in entity_sizes.items():
			if k in images:
				body.append("<pattern id=\"{0}_pattern\" x=\"0\" y=\"0\" width=\"{1}\" height=\"{1}\">".format(k,v))
				body.append("<image xlink:href=\"{0}\" width=\"{1}\" height=\"{1}\"/>".format(images[k], v))
				body.append("</pattern>")

		post = ["</defs>"]

		return pre + body + post
