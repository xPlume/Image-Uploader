from django import forms

from gallery.models import Gallery


class GalleryForm(forms.ModelForm):
	
	class Meta:
		model = Gallery
		fields = ['title']
	#class Meta	
	
#class GalleryForm