import numpy as np
from claims.entities.claim import Claim

class Panel():

	width = Claim.max_inch
	height = Claim.max_inch

	def __init__(self):
		self.map = np.zeros((self.__class__.width, self.__class__.height))
		self.claims = Claim.objects.all()


	def _get_coordinates(self, claim):
		x_initial = claim.y
		y_initial = claim.y + claim.height
		x_final = claim.x
		y_final = claim.x + claim.width
		return x_initial, y_initial, x_final, y_final

	def put_claim(self, claim):
		copy_map = np.zeros((self.__class__.width, self.__class__.height))
		area = claim.get_area()
		x_initial, y_initial, x_final, y_final = self._get_coordinates(claim)
		copy_map[x_initial:y_initial, x_final:y_final] = area
		return copy_map

	def fill_panel(self):
		claims = Claim.objects.all()
		for claim in self.claims:
			panel_claim = self.put_claim(claim)
			self.map = self.map + panel_claim
		return self.map

	def count_occupied_inch(self):
		self.fill_panel()
		busy_inch = self.map[np.where( self.map > Claim.occupied_value )]
		return busy_inch.size

	def get_list_full_claim_ids(self):
		self.fill_panel()
		claims = []
		for claim in self.claims:
			x_initial, y_initial, x_final, y_final = self._get_coordinates(claim)
			inch = self.map[np.where( self.map[x_initial:y_initial, x_final:y_final] > Claim.occupied_value )]
			if len(inch) == 0:
				claims.append(claim.id)
		return claims