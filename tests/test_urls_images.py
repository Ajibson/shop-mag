from django.test import TestCase
from django.urls import reverse, resolve
from django.shortcuts import redirect

from shop_image.views import index
from images.views import upload, delete, update, search, download_image, download_image_payments


""" The tests here are to ensure thata the right views are being served for the url being seen for users app"""


class TestUrl(TestCase):

    def test_url_upload(self):
        url = reverse("images:upload")
        self.assertEqual(resolve(url).func, upload)

    def test_url_delete(self):
        url = reverse('images:delete', args=[1])
        self.assertEqual(resolve(url).func, delete)

    def test_url_update(self):
        url = reverse('images:update', args=[1])
        self.assertEqual(resolve(url).func, update)

    def test_url_search(self):
        url = reverse('images:search')
        self.assertEqual(resolve(url).func, search)

    def test_url_download_image(self):
        url = reverse('images:download_image', args=[1])
        self.assertEqual(resolve(url).func, download_image)

    def test_url_download_payment(self):
        url = reverse('images:download_payment', args=[1])
        self.assertEqual(resolve(url).func, download_image_payments)
