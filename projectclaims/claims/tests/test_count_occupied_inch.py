from rest_framework.test import APITestCase
from claims.tests.factories.claim import ClaimFactory
from claims.entities.panel import Panel
import numpy as np

class TestCountOccupiedInch(APITestCase):

	def setUp(self):
		self.claim_a = ClaimFactory(x=3, y=1, width=4, height=4)
		self.claim_b = ClaimFactory(x=1, y=3, width=4, height=4)
		self.claim_c = ClaimFactory(x=5, y=5, width=2, height=2)
		self.response = 4

	def test_count_occupied_inch(self):
		count = Panel().count_occupied_inch()
		self.assertEqual(self.response, count)