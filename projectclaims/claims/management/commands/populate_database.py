from django.core.management.base import BaseCommand
from claims.models import Claim
import traceback

class Command(BaseCommand):

	help = 'Load csv'

	def handle(self, *args, **options):
		claim = Claim.objects.all().first()
		if not claim:
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
				try:
					claim = Claim(x=x, y=y, width=width, height=height)
					claim.full_clean()
					claim.save()
					print('create', str(line))
				except Exception:
					traceback.print_exc()
					print('not create', str(line))
