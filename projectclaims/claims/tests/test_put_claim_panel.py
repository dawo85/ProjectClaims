from rest_framework.test import APITestCase
from claims.tests.factories.claim import ClaimFactory
from claims.entities.panel import Panel
import numpy as np

class TestPutClaimPanel(APITestCase):

	def setUp(self):
		self.claim = ClaimFactory(x=3, y=2, width=5, height=4)
		self.response = np.zeros((6, 8))
		self.response[2][3] = 1
		self.response[2][4] = 1
		self.response[2][5] = 1
		self.response[2][6] = 1
		self.response[2][7] = 1

		self.response[3][3] = 1
		self.response[3][4] = 1
		self.response[3][5] = 1
		self.response[3][6] = 1
		self.response[3][7] = 1

		self.response[4][3] = 1
		self.response[4][4] = 1
		self.response[4][5] = 1
		self.response[4][6] = 1
		self.response[4][7] = 1

		self.response[5][3] = 1
		self.response[5][4] = 1
		self.response[5][5] = 1
		self.response[5][6] = 1
		self.response[5][7] = 1

	def test_put_claim_panel(self):
		panel_map = Panel().put_claim(self.claim)
		self.assertTrue(np.array_equal(self.response, panel_map))