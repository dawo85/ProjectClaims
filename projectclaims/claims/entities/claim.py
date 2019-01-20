from django.db import models
from django.core.exceptions import ValidationError
import numpy as np

class Claim(models.Model):

	occupied_value = 1
	max_inch = 1000

	x = models.IntegerField()
	y = models.IntegerField()
	width = models.IntegerField()
	height = models.IntegerField()

	def full_clean(self, *args, **kwargs):
		max_width = self.x + self.width
		max_height =  self.y + self.height
		if max_width > self.__class__.max_inch or max_height > self.__class__.max_inch:
			message = 'Incorrect coordinates and size. Panel max size {0} x {0}'.format(str(self.__class__.max_inch))
			raise ValidationError(message)
		super(Claim, self).full_clean(*args, **kwargs)

	def get_area(self):
		area = np.full((self.height, self.width), self.__class__.occupied_value)
		return area