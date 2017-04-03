from ElementProvider import ElementProvider
from ModelRunner import ModelRunner
from BoxDrawer import BoxDrawer
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
		groups = self.model_runner.run(stocks, self.settings)
		boxes = [box for group in groups for box in group.boxes(placements)]

		drawer = BoxDrawer(self.name, self.settings, boxes)
		drawer.draw()

		self.animation_data.updateData(boxes)
		self.animation_data.exportRunData()
		self.adjustRunSpeed(run_speed)

	def adjustRunSpeed(self, run_speed):
		self.animation_data.adjustRunSpeed(run_speed)
		self.animation_data.exportSettings()