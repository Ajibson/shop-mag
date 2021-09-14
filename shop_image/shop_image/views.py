from django.shortcuts import render, redirect
from images.models import Category
from images.forms import ImageForms
from images.models import Image
from django.contrib import messages
# Signup view


def index(request):
    categories = Category.objects.all()
    form = ImageForms()
    images = Image.objects.all()
    context = {
        "categories": categories, 'form': form, 'images': images
    }
    return render(request, 'index.html', context=context)
