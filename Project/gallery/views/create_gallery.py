from django.shortcuts import render, redirect
from django.contrib import messages

from gallery.forms import GalleryForm


def create_gallery(request):
	
	if request.method == 'POST':
		
		new_gallery = GalleryForm(request.POST)
		
		if new_gallery.is_valid():
			new_gallery_instance = new_gallery.save()
			
			messages.success(request, "The gallery was created with success!", extra_tags="success")
			#return redirect('gallery', new_gallery_instance.id)
			return redirect('index')
		#if
		
		else:
			messages.error(request, new_gallery.errors, extra_tags="danger")
			return redirect('create_gallery')
		#else
		
	#if
	
	else:
		new_gallery = GalleryForm()
	#else
	
	
	template_name = "gallery/create_gallery.html"
	context = {
		"new_gallery": new_gallery,
	}
	
	return render(request, template_name, context)
	
#def