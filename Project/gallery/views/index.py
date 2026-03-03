from django.shortcuts import render

from gallery.models import Gallery

def index(request):
	
	all_galleries = Gallery.objects.all()
	
	template_name = "gallery/index.html"
	context = {
		"all_galleries": all_galleries,
	}
	
	return render(request, template_name, context)
	
#def index