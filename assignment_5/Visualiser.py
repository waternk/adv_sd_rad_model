from ElementProvider import ElementProvider
from ModelRunner import ModelRunner
from BoxDrawer import BoxDrawer

class Visualiser(object):
	def visualise(self, model_path, name, width, height):
		provider = ElementProvider(model_path)
		placements = provider.placements()
		stocks = provider.stocks()

		groups = ModelRunner(model_path).run(stocks)
		
		boxes = []
		for group in groups:
			boxes.extend(group.boxes(placements))
		
		drawer = BoxDrawer(name, width, height)
		drawer.draw(boxes)

Visualiser().visualise('ASD_2.mdl', 'index', 750, 750)