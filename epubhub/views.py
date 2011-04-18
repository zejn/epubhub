import os

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from django.views.decorators.cache import cache_page

from epubhub.models import Ebook

class FilterForm(forms.Form):
	q = forms.CharField(max_length=300)

def ebook_list(request):
	form = FilterForm(request.GET)
	q = request.GET.get('q', None)
	if q:
		ebooks = Ebook.objects.filter(path__icontains=q).order_by('path')
	else:
		ebooks = Ebook.objects.all().order_by('-id')[:100]
	
	context = {
		'object_list': ebooks,
		'form': form,
		}
	return render_to_response('epubhub/ebook_list.html', RequestContext(request, context))

def get_ebook(request, object_id):
	e = Ebook.objects.get(pk=object_id)
	response = HttpResponse(mimetype='application/octet-stream')
	response['Content-disposition'] = 'attachment; filename="%s"' % (e.filename,)
	response.write(e.read())
	return response

@cache_page(60*60*24*3) # 3 days
def ebook_convert_mobi(request, object_id):
	e = Ebook.objects.get(pk=object_id)
	response = HttpResponse(mimetype='application/octet-stream')
	response.write(e.convert('mobi'))
	filename = '%s.mobi' % (os.path.splitext(e.filename)[0],)
	response['Content-disposition'] = 'attachment; filename="%s"' % (filename,)
	return response

