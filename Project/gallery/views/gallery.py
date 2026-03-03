from django.shortcuts import render, get_object_or_404

from gallery.models import Gallery
from gallery.models import Image

def gallery(request, gallery_id):
	
	this_gallery = get_object_or_404(Gallery, id=gallery_id)
	
	images = Image.objects.filter(
		gallery=this_gallery,
	)
	
	template_name = "gallery/gallery.html"
	context = {
		"gallery": this_gallery,
		"images": images,
	}
	
	return render(request, template_name, context)
	
#def gallery