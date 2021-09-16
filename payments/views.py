from django.shortcuts import render, redirect
import uuid
from .models import Payment
from images.models import Image, Category
from images.forms import ImageForms
import requests
import json
import os


def initialize_payment(request):
    url = "https://api.paystack.co/transaction/initialize"
    payload = json.dumps({
        "email": "customer@email.com",
        "amount": "500000",
        "reference": uuid.uuid4().hex,
        "metadata": {
            "custom_fields": [
                {
                    "display_name": "Mobile Number",
                    "variable_name": "mobile_number",
                    "value": "+2348012345678"
                }
            ]
        }
    })
    headers = {
        'Authorization': 'Bearer sk_test_bccfb1827d1e81b18073ca06a5239f60ff16740b',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response_url = json.loads(response.text)
    return redirect(response_url['data']["authorization_url"])


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
    image_meant_for.number_of_download += 1
    image_meant_for.save()
    return redirect("images:download_payment", image_meant_for.pk)
