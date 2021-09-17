from django.shortcuts import render, redirect
import uuid
from .models import Payment
from images.models import Image, Category
from images.forms import ImageForms
import requests
import json
import os


def paymnent(request, pk):

    if request.user.is_authenticated:
        email = request.user.email
    else:
        email = "anonymous@mail.com"
    amount = Image.objects.filter(pk=pk).first().price
    reference_id = uuid.uuid4()
    image_meant_for = Image.objects.filter(pk=pk).first()
    image_payment = Payment(image_for=image_meant_for, amount=amount,
                            status='pending', reference_id=reference_id)
    image_payment.save()
    # charge = (0.018 * float(amount)) + float(amount)
    amount = int(amount * 100)  # convert the money to kobo
    key = os.environ.get("key")

    categories = Category.objects.all()
    form = ImageForms()
    images = Image.objects.all()

    context = {
        "email": email,  'amount': amount, 'key': key, 'reference_number': reference_id,
        "categories": categories, 'form': form, 'images': images
    }
    return render(request, 'payments/payment.html', context=context)


def confirm_payment(request, uidb64):
    payment = Payment.objects.filter(reference_id=uidb64).first()
    image_meant_for = payment.image_for
    return redirect("images:download_payment", image_meant_for.pk)
