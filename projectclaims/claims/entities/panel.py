import numpy as np
from claims.entities.claim import Claim

class Panel():

	width = 1000
	height = 1000

	def __init__(self):
		self.map = np.zeros((self.__class__.width, self.__class__.height))

	def put_claim(self, claim):
		copy_map = np.zeros((self.__class__.width, self.__class__.height))
		area = claim.get_area()
		x_initial = claim.y
		y_initial = claim.y + claim.height
		x_final = claim.x
		y_final = claim.x + claim.width
		copy_map[x_initial:y_initial, x_final:y_final] = area
		return copy_map

	def fill_panel(self):
		claims = Claim.objects.all()
		for claim in claims:
			panel_claim = self.put_claim(claim)
			self.map = self.map + panel_claim
		return self.map

