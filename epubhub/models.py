import zipfile
import os
from django.db import models
from django.conf import settings
import tempfile
import subprocess

EBOOK_CONVERT = '/usr/bin/ebook-convert'

class Ebook(models.Model):
	archive = models.CharField(max_length=200)
	path = models.CharField(max_length=800)
	
	def read(self):
		archive_path = os.path.join(settings.EPUBHUB_DATA_DIR, self.archive)
		zf = zipfile.ZipFile(open(archive_path))
		return zf.read(self.path)
	
	def filename():
		def get(self):
			return os.path.basename(self.path)
		return (get, None, None)
	filename = property(*filename())
	
	def convert(self, fmt):
		assert fmt in ('mobi',)
		basename, ext = os.path.splitext(self.filename)
		
		extracted = tempfile.NamedTemporaryFile(prefix='/tmp/epubhub-', suffix=ext)
		extracted.write(self.read())
		extracted.flush()
		extracted.seek(0)
		
		converted = tempfile.NamedTemporaryFile(prefix='/tmp/epubhub-', suffix='.%s' % (fmt,))
		
		cmd = [EBOOK_CONVERT, extracted.name, converted.name]
		p = subprocess.Popen(cmd)
		p.wait()
		converted.seek(0)
		return converted.read()









