class VisualisationSettings(object):
	def __init__(self, width, height, ball_rows, ball_cols):
		self.width = width
		self.height = height
		self.ball_rows = ball_rows
		self.ball_cols = ball_cols
		self.max_entities = ball_rows * ball_cols