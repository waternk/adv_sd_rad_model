from ElementProvider import ElementProvider
from ModelRunner import ModelRunner
from BoxDrawer import BoxDrawer
import json

class BallCountExporter(object):
	def export(self, boxes):
		data_dict = {}
		for box in boxes:
			data_dict[box.name] = list(box.run_data)

		data_string = 'run_data = ' + json.dumps(data_dict)

		with open("run_data.js", "w") as file:
			file.write(data_string)

class VisualisationSettings(object):
	def __init__(self, width, height, box_rows, box_cols, ball_rows, ball_cols):
		self.width = width
		self.height = height
		self.box_rows = box_rows
		self.box_cols = box_cols
		self.ball_rows = ball_rows
		self.ball_cols = ball_cols

class Visualiser(object):
	def visualise(self, model_path, name, settings):
		provider = ElementProvider(model_path)
		placements = provider.placements()
		stocks = provider.stocks()

		groups = ModelRunner(model_path).run(stocks, settings.ball_rows, settings.ball_cols)
		
		boxes = [box for group in groups for box in group.boxes(placements)]
		
		BallCountExporter().export(boxes)

		drawer = BoxDrawer(name, settings.width, settings.height, settings.box_rows, settings.box_cols)
		drawer.draw(boxes)

settings = VisualisationSettings(750, 750, 1, 3, 10, 10)
Visualiser().visualise('ASD_2.mdl', 'index', settings)