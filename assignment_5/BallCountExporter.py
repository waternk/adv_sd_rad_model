import json

class BallCountExporter(object):
	def export(self, run_speed, boxes):
		
		data_dict = {}
		run_length = 0
		for box in boxes:
			data = list(box.run_data)
			run_length = max(len(data), run_length)
			data_dict[box.name] = data

		data_string = 'run_data = ' + json.dumps(data_dict)

		with open("run_data.js", "w") as file:
			file.write(data_string)

		settings_string = 'run_settings = ' + json.dumps({'run_length' : run_length, 'run_speed': run_speed})

		with open("run_settings.js", "w") as file:
			file.write(settings_string)