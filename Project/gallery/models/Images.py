from django.db import models
import os

from gallery.models import Gallery

# Saving the images in a specific folder: ~/[gallery.id]-[gallery.title] / [img_name]
def specific_folder(instance, filename):
	sanitized_title = ''.join(e for e in instance.gallery.title if e.isalnum())
	return os.path.join('gallery', f"{instance.gallery.id}-{sanitized_title}", filename)
#def 


# The images of a Gallery
class Image(models.Model):
	
	gallery = models.ForeignKey(Gallery, related_name="images", on_delete=models.CASCADE)
	image = models.ImageField(upload_to=specific_folder)
	order = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return f"Image n°{self.order}"
	#def
	
	class Meta:
		ordering = ["order"]
	#class Meta
	
	
	# When deleting image reference, delete image from media folder 
	def delete(self, *args, **kwargs):
		if self.image and os.path.isfile(self.image.path):
			os.remove(self.image.path)
		#if
		super().delete(*args, **kwargs)
	#def
	
	
	
#class Image
