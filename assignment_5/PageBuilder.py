from SVGElement import quotify

class PageBuilder(object):
	def build(self, name, body):
		pre = ["<!DOCTYPE html>", "<html>", "<head>", 
			"<link rel=\"stylesheet\" href=\"{0}_style.css\"/>".format(name),
			"<script src=\"snap.svg-min.js\"></script>",
			"<script src=\"animation.js\"></script>",
			"<script src=\"run_data.js\"></script>",
			"<script src=\"run_settings.js\"></script>",
			"</head>", "<body>",
			"<div id=\"content\">",
			"<div class=\"header\"><img src=\"images/venvis.png\" /><H1>{0}</H1></div>".format(name),
			"<div id=\"progress\"><div id=\"progress_bar\"><H3 id=\"timer\">0</H3></div></div>"]
			
		post = ["<div id=\"buttons\">",
				"<button id=\"play\" type=\"button\"></button>",
				"<button id=\"pause\" type=\"button\"></button>",
				"<button id=\"stop\" type=\"button\"></button>",
				"<button id=\"replay\" type=\"button\"></button>",
				"</div>", "<p>VenVis 2017</p>", "</div>", "</body>", "</html>"]

		return pre + body + post

class SVGBuilder(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def build(self, svg_elements, entity_sizes, background_sizes, entity_images, background_images):
		pre = ["<svg id=\"animation_svg\" width={0} height={1}>".format(quotify(self.width), quotify(self.height))]

		patterns = self.buildPatterns(entity_sizes, background_sizes, entity_images, background_images)
		elements = list(map(lambda e: e.text(), svg_elements))
		post = ["</svg>"]

		return pre + patterns + elements + post

	def buildPatterns(self, entity_sizes, background_sizes, entity_images, background_images):
		pre = ["<defs>"]

		body = []
		for k,v in entity_sizes.items():
			if k in entity_images:
				body.append("<pattern id=\"{0}_pattern\" x=\"0\" y=\"0\" width=\"1\" height=\"1\">".format(k,v))
				body.append("<image xlink:href=\"{0}\" width=\"{1}\" height=\"{1}\"/>".format(entity_images[k], v))
				body.append("</pattern>")

		for k,v in background_sizes.items():
			if k in background_images:
				body.append("<pattern id=\"{0}_background_pattern\" x=\"0\" y=\"0\" width=\"1\" height=\"1\">".format(k,v))
				body.append("<image xlink:href=\"{0}\" width=\"{1}\" height=\"{1}\"/>".format(background_images[k], v))
				body.append("</pattern>")

		post = ["</defs>"]

		return pre + body + post
