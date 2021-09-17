from django.test import TestCase, Client
from django.urls import reverse
from images.models import Image
from users.models import User


class ViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.upload_url = reverse("images:upload")
        self.delete_url = reverse('images:delete', args=[1])
        self.update_url = reverse('images:update', args=[1])
        self.search_url = reverse('images:search')
        self.download_image_url = reverse('images:download_image', args=[1])
        self.download_payment_url = reverse(
            'images:download_payment', args=[1])
        self.user = User.objects.create(email="az@mail.com")
        self.user1 = User.objects.create(email="azs@mail.com")
        self.image = Image.objects.create(price=20, user=self.user)

    def test_upload_temmplate(self):
        response = self.client.get(self.upload_url)
        # self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_delete_redirect(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_update_redirect(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 302)

    def test_search_template(self):
        response = self.client.get(self.search_url, data={
                                   "search_value": "model"})
        self.assertTemplateUsed(response, 'index.html')

    def test_download_image_redirect(self):
        response = self.client.get(self.download_image_url)
        self.assertEqual(response.status_code, 302)

    def test_download_image_user_count(self):
        qs = Image.objects.filter(user=self.user)
        self.assertEqual(qs.count(), 1)

    def test_download_image_user_exist(self):
        qs = Image.objects.filter(user=self.user1)
        self.assertFalse(qs.exists())
