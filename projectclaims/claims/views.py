from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from claims.models import Panel

class OccupiedInchView(APIView):

	def get(self, request):
		result = {
			'count': Panel().count_occupied_inch()
		}
		return Response(result)

class ListFullClaimIds(APIView):

	def get(self, request):
		result = {
			'claim_ids': Panel().get_list_full_claim_ids()
		}
		return Response(result)
		