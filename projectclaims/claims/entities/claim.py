from django.db import models
import numpy as np

class Claim(models.Model):

	busy_value = 1
	x = models.IntegerField()
	y = models.IntegerField()
	width = models.IntegerField()
	height = models.IntegerField()

	def get_area(self):
		area = np.full((self.height, self.width), self.__class__.busy_value)
		return area