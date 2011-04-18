
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	def handle(self, *args, **options):
		import os
		import zipfile
		from django.conf import settings
		from epubhub.models import Ebook
		
		if args:
			files = args
		else:
			files = os.listdir(settings.EPUBHUB_DATA_DIR)
		
		for name in files:
			fn = os.path.join(settings.EPUBHUB_DATA_DIR, name)
			if zipfile.is_zipfile(fn):
				zf = zipfile.ZipFile(open(fn))
				for info in zf.infolist():
					if info.flag_bits == 2: # is file
						eb, created = Ebook.objects.get_or_create(path=info.filename, archive=name)
						if created:
							eb.save()
							print name, info.filename


