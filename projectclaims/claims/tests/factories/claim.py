from factory.django import DjangoModelFactory
from claims.models import Claim


class ClaimFactory(DjangoModelFactory):

	class Meta:
		model = Claim