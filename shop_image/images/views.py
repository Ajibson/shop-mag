from django.shortcuts import render, redirect
from .forms import ImageForms
from django.contrib import messages
from images.models import Category
from .models import Image
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from images.models import Image, Category
from images.forms import ImageForms
import mimetypes


def upload(request):
    form = ImageForms()

    if request.method == "POST":
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            save_obj = form.save(commit=False)
            save_obj.user = request.user
            save_obj.save()
            return redirect('users:dashboard')
        else:
            print(form)
            messages.error(request, "Upload failed")
    categories = Category.objects.all()
    context = {
        "categories": categories, "form": form
    }
    return render(request, 'index.html', context)


@login_required()
def delete(request, pk):
    image_to_delete = Image.objects.filter(pk=pk).first()
    if request.user == image_to_delete.user:
        image_to_delete.delete()
        messages.success(request, "Image deleted successfully")
    else:
        messages.error(request, "You can't delete this image")
    return redirect("users:dashboard")


@login_required()
def update(request, pk):
    if request.method == "POST":
        instance = Image.objects.filter(pk=pk).first()

        form = ImageForms(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            save_obj = form.save(commit=False)
            save_obj.user = request.user
            save_obj.save()
            messages.success(request, "Image updated successfully")
            return redirect('users:dashboard')
        else:
            messages.error(request, "Upload failed")
            return redirect("users:dashboard")


def search(request):
    # I am assuming space separator in URL like "random stuff"
    q = request.GET['search_value'].split(",")
    query = Q()
    for word in q:  # if user input 'python django' q = ['python', 'django']
        query = query | Q(image_name__icontains=word) | Q(
            image_category__name__icontains=word) | Q(price__contains=word)
    images = Image.objects.filter(query).distinct()

    if not images:
        images = Image.objects.all()

    categories = Category.objects.all()
    form = ImageForms()
    context = {
        "categories": categories, 'form': form, 'images': images
    }
    return render(request, 'index.html', context=context)


def download_image(request, pk):
    instance = Image.objects.filter(pk=pk).first()
    fl_path = instance.image
    filename = ‘downloaded_file_name.extension’

    fl = open(fl_path, 'r’)
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
