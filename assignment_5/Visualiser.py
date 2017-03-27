from ElementProvider import ElementProvider
from ModelRunner import ModelRunner
from BoxDrawer import BoxDrawer
from BallCountExporter import BallCountExporter

class VisualisationSettings(object):
	def __init__(self, width, height, box_rows, box_cols, ball_rows, ball_cols, run_speed):
		self.width = width
		self.height = height
		self.box_rows = box_rows
		self.box_cols = box_cols
		self.ball_rows = ball_rows
		self.ball_cols = ball_cols
		self.run_speed = run_speed

class Visualiser(object):
	def visualise(self, model_path, name, settings):
		provider = ElementProvider(model_path)
		placements = provider.placements()
		stocks = provider.stocks()

		groups = ModelRunner(model_path).run(stocks, settings.ball_rows, settings.ball_cols)
		
		boxes = [box for group in groups for box in group.boxes(placements)]
		
		BallCountExporter().export(settings.run_speed, boxes)

		drawer = BoxDrawer(name, settings.width, settings.height, settings.box_rows, settings.box_cols)
		drawer.draw(boxes)

settings = VisualisationSettings(750, 750, 1, 3, 10, 10, 1000)
Visualiser().visualise('ASD_2.mdl', 'index', settings)