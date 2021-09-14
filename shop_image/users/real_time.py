from django.http import HttpResponse
import json
from .models import User


def check_user_email(request, status):
    response = {}
    if status == "email":
        email = request.GET.get('email')
        try:
            email_check = User.objects.get(email=email)
            response['response'] = 'not valid'
            return response
        except User.DoesNotExist:
            response['response'] = "valid"
            return response
    elif status == "password":
        password = request.GET.get('password')
        if len(password) < 8:
            response['response'] = "not valid"
        elif password.isalpha() and password.isnumeric():
            response['response'] = "not valid"
        else:
            response['response'] = "valid"

        return response
