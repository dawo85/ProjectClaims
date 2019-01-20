from django.db import models
from claims.entities.panel import Panel
import numpy as np

class Claim(models.Model):

	x = models.IntegerField()
	y = models.IntegerField()
	width = models.IntegerField()
	height = models.IntegerField()

	def get_area(self):
		area = np.full((self.height, self.width), Panel.busy_value)
		return area