from django.urls import path

# Import the views
from .views import (signup, Login, password_reset_request, check_password,
                    password_reset_confirm, dashboard, Logout, check_email, message_admin)
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    # Authentication urls
    path('register/', signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('message-admin/', message_admin, name="message"),
    path('check_email/<str:status>', check_email, name="check"),
    path("password_reset/", password_reset_request, name="reset_password"),
    path('reset/<uidb64>/<token>/', password_reset_confirm,
         name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
