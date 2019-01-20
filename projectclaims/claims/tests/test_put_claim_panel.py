from rest_framework.test import APITestCase
from claims.tests.factories.claim import ClaimFactory
from claims.entities.panel import Panel
import numpy as np

class TestPutClaimPanel(APITestCase):

	def setUp(self):
		self.claim_a = ClaimFactory(x=1, y=2, width=3, height=2)
		self.response_a = np.zeros((1000, 1000))
		self.response_a[2][1] = 1
		self.response_a[3][1] = 1
		self.response_a[2][2] = 1
		self.response_a[3][2] = 1
		self.response_a[2][3] = 1
		self.response_a[3][3] = 1
		self.claim_b = ClaimFactory(x=100, y=5, width=1, height=5)
		self.response_b = np.zeros((1000, 1000))
		self.response_b[5][100] = 1
		self.response_b[6][100] = 1
		self.response_b[7][100] = 1
		self.response_b[8][100] = 1
		self.response_b[9][100] = 1

	def test_put_claim_panel(self):
		panel_map = Panel().put_claim(self.claim_a)
		self.assertTrue(np.array_equal(self.response_a, panel_map))
		panel_map = Panel().put_claim(self.claim_b)
		self.assertTrue(np.array_equal(self.response_b, panel_map))