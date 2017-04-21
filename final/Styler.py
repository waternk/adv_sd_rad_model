class Styler(object):
	def __init__(self, units, width):

		default_styles = [
			"#content {{ margin: 0 auto; width:{0}px; border: 1px solid #DDDDDD; padding: 10px; box-shadow: 10px 10px 5px #888888; }}".format(width),
			"#buttons { margin: auto; width:40%; padding-top: 10px; text-align: center; }",
			"button { padding: 0; border: none; background: none; }",
			"button :hover { border: 1px solid blue; }",
			".header img { float: right; height: 50px; }",
			".header h1 { position: relative; top: 18px; left: 10px; }",
			"#play { background:url(images/play.png) no-repeat; width: 40px; height: 40px; background-size: 100%; margin-right: 10px; }",
			"#pause { background:url(images/pause.png) no-repeat; width: 40px; height: 40px; background-size: 100%; margin-right: 10px; }",
			"#stop { background:url(images/stop.png) no-repeat; width: 40px; height: 40px; background-size: 100%; margin-right: 10px; }",
			"#replay { background:url(images/replay.png) no-repeat; width: 40px; height: 40px; background-size: 100%; }",
			"svg { background-color:rgb(255,255,255);margin-left:auto; margin-right:auto; display:block;}",
			"h1 { text-align: center; font-family: Roboto, Helvetica, Arial, sans-serif; }",
			"h3 { font-family: Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 0; }",
			"#partial { fill:rgb(230,230,230); }",
			".box { fill:rgba(0,0,0,0); stroke:rgba(0,0,0,0.2); stroke-width:1; }",
			".popup_text { color:rgb(255,255,255); background-color:rgb(0,0,0); opacity: 0.75; text-align: center; height: 100%; width: 100%; display: table; }",
			".popup_text h1 { display: table-cell; font-size: 1.2em; text-align: center; vertical-align: middle; }",
			"#progress { border:1px solid #ccc; }",
			"#progress_bar { margin: 0; padding: 0; width: 0%; background-color: #ccc; text-align: center; }"
		]

		entity_styles = list(map(lambda u: ".{0} {{ fill:url(#{0}_pattern) }}".format(u), units))

		background_styles = list(map(lambda u: "#{0}_placement {{ fill:url(#{0}_background_pattern) }}".format(u), units))

		self.styles = default_styles + entity_styles + background_styles

	def save(self, name):
		with open('{0}_style.css'.format(name), 'w') as file: 
			for line in self.styles:
				file.write(line + '\n')