import json
from VisualisationSettings import VisualisationSettings

class AnimationData(object):
	def __init__(self, settings):
		self.max_entities = settings.max_entities
		self.run_speed = 1000
		self.run_length = 0
		self.run_data = {}

	def updateData(self, boxes):
		self.run_data.clear()
		run_length = 0

		for box in boxes:
			data = list(box.run_data)
			run_length = max(len(data), run_length)
			self.run_data[box.name] = data

		self.run_length = run_length

	def adjustRunSpeed(self, run_speed):
		self.run_speed = run_speed

	def exportRunData(self):
		data_string = 'run_data = ' + json.dumps(self.run_data)

		with open("run_data.js", "w") as file:
			file.write(data_string)

	def exportSettings(self):
		settings = {
			'run_length' : self.run_length, 
			'run_speed': self.run_speed,
			'max_entities': self.max_entities
		}

		settings_string = 'run_settings = ' + json.dumps(settings)

		with open("run_settings.js", "w") as file:
			file.write(settings_string)