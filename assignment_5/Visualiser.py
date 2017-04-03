from ElementProvider import ElementProvider
from ModelRunner import ModelRunner
from GroupDrawer import GroupDrawer
from AnimationData import AnimationData
from VisualisationSettings import VisualisationSettings

class Visualiser(object):
	def __init__(self, name, model_path, settings):
		self.name = name
		self.provider = ElementProvider(model_path)
		self.model_runner = ModelRunner(model_path)
		self.animation_data = AnimationData(settings)
		self.settings = settings

	def visualise(self, run_speed = 1000):
		(placements, stocks, _) = self.provider.provide()
		groups = self.model_runner.run(stocks, placements, self.settings)
		drawer = GroupDrawer(self.name, self.settings, groups)
		drawer.draw()

		self.animation_data.updateData(groups)
		self.animation_data.exportRunData()
		self.adjustRunSpeed(run_speed)

	def adjustRunSpeed(self, run_speed):
		self.animation_data.adjustRunSpeed(run_speed)
		self.animation_data.exportSettings()

width = 400
height = 400
ball_rows = 8
ball_cols = 8

settings = VisualisationSettings(width, height, ball_rows, ball_cols)
visualiser = Visualiser('index', 'ASD_2.mdl', settings)
visualiser.visualise()