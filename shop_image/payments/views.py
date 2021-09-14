from django.shortcuts import render, redirect
import uuid
from .models import Payment
from images.models import Image


def paymnent(request, pk):

    email = request.user.email
    amount = Image.objects.filter(pk=pk).first().price
    reference_id = uuid.uuid4()
    image_meant_for = Image.objects.filter(pk=pk).first()
    image_payment = Payment(image_for=image_meant_for, amount=amount,
                            status='pending', reference_id=reference_id)
    image_payment.save()
    # charge = (0.018 * float(amount)) + float(amount)
    amount = int(amount * 100)  # convert the money to kobo
    # os.environ.get("key")
    key = "pk_test_ecfda66835b5d8dd6f50342b4f6531f3e9efdc69"
    context = {
        "email": email,  'amount': amount, 'key': key, 'reference_number': reference_id,
    }
    return render(request, 'payments/payment.html', context=context)


def confirm_payment(request, uidb64):
    payment = Payment.objects.filter(reference_id=uidb64).first()
    image_meant_for = payment.image_for
    image_meant_for.number_of_download += 1
    image_meant_for.save()
    return redirect("index")
