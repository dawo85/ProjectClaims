from rest_framework.test import APITestCase
from claims.tests.factories.claim import ClaimFactory
from claims.entities.panel import Panel
import numpy as np

class TestFillPanel(APITestCase):

	def setUp(self):
		self.claim_a = ClaimFactory(x=3, y=1, width=4, height=4)
		self.claim_b = ClaimFactory(x=1, y=3, width=4, height=4)
		self.claim_c = ClaimFactory(x=5, y=5, width=2, height=2)
		self.response = np.zeros((7, 7))
		self.response[1][3]=1
		self.response[1][4]=1
		self.response[1][5]=1
		self.response[1][6]=1

		self.response[2][3]=1
		self.response[2][4]=1
		self.response[2][5]=1
		self.response[2][6]=1

		self.response[3][1]=1
		self.response[3][2]=1
		self.response[3][3]=2
		self.response[3][4]=2
		self.response[3][5]=1
		self.response[3][6]=1

		self.response[4][1]=1
		self.response[4][2]=1
		self.response[4][3]=2
		self.response[4][4]=2
		self.response[4][5]=1
		self.response[4][6]=1

		self.response[5][1]=1
		self.response[5][2]=1
		self.response[5][3]=1
		self.response[5][4]=1
		self.response[5][5]=1
		self.response[5][6]=1

		self.response[6][1]=1
		self.response[6][2]=1
		self.response[6][3]=1
		self.response[6][4]=1
		self.response[6][5]=1
		self.response[6][6]=1

	def test_fill_panel(self):
		panel_map = Panel().fill_panel()
		self.assertTrue(np.array_equal(self.response, panel_map))