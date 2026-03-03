import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.http import require_POST


from gallery.models import Gallery, Image


# Upload / Delete / Reorder images on an existing Gallery.
def gallery_edit(request, gallery_id):
	
	gallery = get_object_or_404(Gallery, id=gallery_id)
	
	if request.method == "POST":
		
		# 1) Delete any existing images the user marked for removal
		to_remove = json.loads(request.POST.get("remove_ids", "[]"))
		if to_remove:
			for img in Image.objects.filter(pk__in=to_remove, gallery=gallery):
				img.delete()
			#for
		#if
		
		
		# 2) Collect newly uploaded files
		new_files = request.FILES.getlist("new_images")
		new_objs = [Image(gallery=gallery, image=f) for f in new_files]
		
		
		# 3) Build maps of existing & new images for ordering
		existing_qs = gallery.images.all()  # after deletions
		existing_map = {img.pk: img for img in existing_qs}
		new_map = {str(idx): img for idx, img in enumerate(new_objs)}
		
		
		# 4) Parse the final order from the hidden JSON
		order_list = json.loads(request.POST.get("order", "[]"))
		for position, item in enumerate(order_list):
			if "id" in item:
				img = existing_map.get(item["id"])
			#if
			else:  # temp_index for new files
				img = new_map.get(str(item.get("temp_index")))
			#else
			if img:
				img.order = position
			#if
		#for
		
		
		# 5) Persist everything
		if existing_map:
			Image.objects.bulk_update(existing_map.values(), ["order"])
		#if
		if new_objs:
			Image.objects.bulk_create(new_objs)
		#if
		
		messages.success(request, "The modifications have been saved!", extra_tags="success")
		return redirect("gallery", gallery_id=gallery.id)
	# if
	
	# GET : render the uploader with previews of current images
	existing_images = [
		{"id": img.pk, "url": img.image.url, "order": img.order}
		for img in gallery.images.all()
	]
	
	
	template_name = "gallery/gallery_edit.html"
	context = {
		"gallery": gallery,
		"existing_images_json": json.dumps(existing_images),
	}
	
	return render(request, template_name, context)
	
#def gallery_edit


@require_POST
def image_delete_ajax(request):
	"""
	AJAX endpoint to delete an existing image immediately.
	"""
	img_id = request.POST.get("id")
	img = get_object_or_404(Image, pk=img_id)
	img.delete()
	return JsonResponse({"status": "ok", "id": img_id})
#def image_delete_ajax