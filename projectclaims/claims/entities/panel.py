import numpy as np

class Panel():

	width = 1000
	height = 1000
	busy_value = 1

	def __init__(self):
		self.map = np.zeros((self.__class__.width, self.__class__.height))

	def put_claim(self, claim):
		copy_map = np.copy(self.map)
		area = claim.get_area()
		x_initial = claim.y
		y_initial = claim.y + claim.height
		x_final = claim.x
		y_final = claim.x + claim.width
		copy_map[x_initial:y_initial, x_final:y_final] = area
		return copy_map