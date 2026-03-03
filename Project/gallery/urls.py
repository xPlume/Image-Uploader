from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("create-gallery", views.create_gallery, name="create_gallery"),
	path("gallery/<int:gallery_id>", views.gallery, name="gallery"),
	path("edit-gallery/<int:gallery_id>", views.gallery_edit, name="gallery_edit"),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
