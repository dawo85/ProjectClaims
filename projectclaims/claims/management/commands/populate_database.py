from django.core.management.base import BaseCommand
from claims.models import Claim

class Command(BaseCommand):

	help = 'Load csv'

	def handle(self, *args, **options):
		namefile = '/code/claims/management/commands/technical_test_input.in'
		mode = 'r'
		file_csv = open(namefile, mode)
		for line in file_csv:
			info = line.split(':')
			coordinates = info[0].split('@')[1].strip().split(',')
			size = info[1].strip().split('x')
			y = int(coordinates[0])
			x = int(coordinates[1])
			width = int(size[0])
			height = int(size[1])
			claim = Claim(x=x, y=y, width=width, height=height)
			claim.save()