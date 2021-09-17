from django.test import TestCase
from payments.views import paymnent, confirm_payment
from django.urls import reverse, resolve


class PaymentTest(TestCase):

    def test_payment(self):
        url = reverse("payments:payment", args=[2])
        self.assertEqual(resolve(url).func, paymnent)

    def test_confirm_payment(self):
        url = reverse("payments:confirm_payment", args=['sksklffkffll'])
        self.assertEqual(resolve(url).func, confirm_payment)
