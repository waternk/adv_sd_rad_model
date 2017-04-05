from SVGElement import quotify

class PageBuilder(object):
	def build(self, name, body):
		pre = ["<!DOCTYPE html>", "<html>", "<head>", 
			"<link rel=\"stylesheet\" href=\"style.css\"/>",
			"<script src=\"snap.svg-min.js\"></script>",
			"<script src=\"animation.js\"></script>",
			"<script src=\"run_data.js\"></script>",
			"<script src=\"run_settings.js\"></script>",
			"</head>", "<body>",
			"<div id=\"content\">",
			"<H1>{0}</H1>".format(name),
			"<H3 id=\"timer\">0</H3>"]
			
		post = ["<div id=\"buttons\">",
			"<button id=\"play\" type=\"button\">Play</button>",
			"<button id=\"pause\" type=\"button\">Pause</button>",
			"<button id=\"stop\" type=\"button\">Stop</button>",
			"</div>", "</div>", "</body>", "</html>"]

		return pre + body + post

class SVGBuilder(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def build(self, svg_elements, entity_sizes, images, backgrounds):
		pre = ["<svg id=\"animation_svg\" width={0} height={1}>".format(quotify(self.width), quotify(self.height))]

		background_size = 159

		patterns = self.buildPatterns(entity_sizes, background_size, images, backgrounds)
		elements = list(map(lambda e: e.text(), svg_elements))
		post = ["</svg>"]

		return pre + patterns + elements + post

	def buildPatterns(self, entity_sizes, background_size, images, backgrounds):
		pre = ["<defs>"]

		body = []
		for k,v in entity_sizes.items():
			if k in images:
				body.append("<pattern id=\"{0}_pattern\" x=\"0\" y=\"0\" width=\"{1}\" height=\"{1}\">".format(k,v))
				body.append("<image xlink:href=\"{0}\" width=\"{1}\" height=\"{1}\"/>".format(images[k], v))
				body.append("</pattern>")

				body.append("<pattern id=\"{0}_background_pattern\" x=\"0\" y=\"0\" width=\"{1}\" height=\"{1}\">".format(k,background_size))
				body.append("<image xlink:href=\"{0}\" width=\"{1}\" height=\"{1}\"/>".format(backgrounds[k], background_size))
				body.append("</pattern>")

		post = ["</defs>"]

		return pre + body + post
