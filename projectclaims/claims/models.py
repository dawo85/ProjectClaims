from django.db import models

class Claim(models.Model):

	x = models.IntegerField()
	y = models.IntegerField()
	width = models.IntegerField()
	height = models.IntegerField()