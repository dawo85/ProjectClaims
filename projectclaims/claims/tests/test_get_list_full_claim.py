from rest_framework.test import APITestCase
from claims.tests.factories.claim import ClaimFactory
from claims.entities.panel import Panel
import numpy as np

class TestGetListFullClaim(APITestCase):

	def setUp(self):
		self.claim_a = ClaimFactory(x=3, y=1, width=4, height=4)
		self.claim_b = ClaimFactory(x=1, y=3, width=4, height=4)
		self.claim_c = ClaimFactory(x=5, y=5, width=2, height=2)
		self.total_id = 1

	def test_get_list_full_claim(self):
		ids_claims = Panel().get_list_full_claim_ids()
		self.assertEqual(self.total_id, len(ids_claims))
		self.assertEqual(self.claim_c.id, ids_claims[0])

