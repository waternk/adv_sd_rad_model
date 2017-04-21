import os.path

class LibraryManager(object):
	def checkDependencies(self):
		if os.path.exists('snap.svg-min.js'):
			return
		else:
			print("Missing the Snap.SVG library - Please include the minified js version in this folder")