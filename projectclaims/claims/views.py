from django.shortcuts import render
from rest_framework.views import APIView
from claims.models import Claim
from rest_framework.response import Response
from django.db.models import Sum

class OccupiedInchView(APIView):

	def get(self, request):
		result = {}
		return Response(result)