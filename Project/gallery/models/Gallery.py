from django.db import models


# Defining the existance of a Gallery
class Gallery(models.Model):
	
	title = models.CharField(max_length=200)
	
	def __str__(self):
		return f"Gallery: {self.title}"
	#def
	
#class Gallery