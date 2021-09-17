from django.test import TestCase, Client
from django.urls import reverse
from images.models import Image
from users.models import User
from payments.models import Payment


class ViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="az@mail.com")
        self.user1 = User.objects.create(email="azs@mail.com")
        self.image = Image.objects.create(
            price=20, user=self.user, image="https://res.cloudinary.com/hrh5zmmzu/image/upload/v1/media/course_pics/aspen_rryxa6")
        self.payment_url = reverse("payments:payment", args=[1])
        self.confirm_payment_url = reverse(
            'payments:confirm_payment', args=["fabfd1ed-b98b-4174-b181-1f2f60a27d21"])

    def test_payment_temmplate(self):
        response = self.client.get(self.payment_url)
        self.assertTemplateUsed(response, 'payments/payment.html')

    def test_confirm_payment(self):
        response = self.client.get(self.payment_url)
        self.assertEqual(response.status_code, 200)
