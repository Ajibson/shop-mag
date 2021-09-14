from django.urls import path

# Import the views
from .views import paymnent, confirm_payment

app_name = "payments"

urlpatterns = [
    path('payment/<int:pk>/', paymnent, name='payment'),
    path("confirm_payment/<uidb64>/",
         confirm_payment, name="confirm_payment")
]
