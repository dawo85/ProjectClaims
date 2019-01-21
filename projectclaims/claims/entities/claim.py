from django.db import models
from django.core.exceptions import ValidationError
import numpy as np

class Claim(models.Model):

	occupied_value = 1

	x = models.IntegerField()
	y = models.IntegerField()
	width = models.IntegerField()
	height = models.IntegerField()

	def get_area(self):
		area = np.full((self.height, self.width), self.__class__.occupied_value)
		return area