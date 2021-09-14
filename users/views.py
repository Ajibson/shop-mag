from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SignUpForm, LoginForm, PasswordChangeForm, ResetForms, NewPasswordResetForm, MessageForm
from .models import User
from .models import passwordresetcode
from django.contrib import messages
from .email import password_reset_email
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
import uuid
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .real_time import check_user_email
from images.models import Image, Category
from images.forms import ImageForms


# Signup view
def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            # handdle the form saving to hash the password instead of saving raw password
            save_form = form.save(commit=False)
            save_form.set_password(form.cleaned_data['password'])
            save_form.save()
            messages.success(request, "Registration completed successfully")
            login(request, save_form)
            return redirect('index')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def Login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Wrong credentials provided")
                return redirect('users:login')

    return render(request, 'users/login.html')


def Logout(request):
    logout(request)
    return redirect('index')


def message_admin(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.sender = request.user
            save_form.save()
            messages.success(request, "Message sent successfully")
            return redirect("users:dashboard")


@login_required()
def dashboard(request):
    user_images = Image.objects.filter(user=request.user)
    categories = Category.objects.all()
    form = ImageForms()
    context = {
        "images": user_images, "form": form, "categories": categories
    }
    return render(request, 'users/dashboard.html', context)


def check_email(request, status):
    response = check_user_email(request, status)
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


def check_password(request):
    check_user_password(request)


def password_reset_request(request):
    if request.method == "POST":
        form = ResetForms(request.POST)
        if form.is_valid():
            gotten_email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=gotten_email)
                if user:
                    send_email = password_reset_email(user)
                    return redirect("password_reset_done")
                else:
                    messages.error(request, 'The email is not registered')
                    return redirect('reset_password')
            except User.DoesNotExist:
                messages.error(request, 'The email is not registered')
                return redirect('reset_password')
        pass

    return render(request, "users/password_reset_form.html")


def password_reset_confirm(request, uidb64, token):
    user_pk = force_text(urlsafe_base64_decode(uidb64))
    try:
        user = User.objects.get(pk=1)
        if request.method == 'POST':
            form = NewPasswordResetForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password2']
                user.set_password(password)
                user.save()
                return redirect('password_reset_complete')
            else:
                return render(request, 'users/password_reset_confirm.html', {'form': form})
        else:
            get_token = passwordresetcode.objects.get(code=token)
            date = timezone.now() - get_token.created_at
            if user and get_token:
                if date.seconds > 3600:  # 7 min set for link expiration
                    get_token.delete()
                    messages.error(request, "Reset link has expired")
                    return redirect('reset_password')
                else:
                    get_token.delete()
                    form = NewPasswordResetForm()
                    return render(request, 'users/password_reset_confirm.html', {'form': form})
    except (User.DoesNotExist, passwordresetcode.DoesNotExist):
        messages.error(request, "Reset link has been revoked")
        return redirect('reset_password')
