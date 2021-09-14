from django.test import TestCase
from django.urls import reverse, resolve
from django.shortcuts import redirect

from shop_image.views import index
from ..views import signup, Login, Logout, dashboard, password_reset_request, password_reset_confirm
from django.contrib.auth import views as auth_views

""" The tests here are to ensure thata the right views are being served for the url being seen for users app"""


class TestUrl(TestCase):

    def test_url_home(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)

    def test_url_signup(self):
        url = reverse('users:signup')
        self.assertEqual(resolve(url).func, signup)

    def test_url_login(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, Login)

    def test_url_logout(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, Logout)

    def test_url_dashboard(self):
        url = reverse('users:dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_url_password_reset_request(self):
        url = reverse('users:reset_password')
        self.assertEqual(resolve(url).func, password_reset_request)

    def test_url_password_reset_confirm(self):
        url = reverse('users:password_reset_confirm', args=[
                      '2371a3d2-e218-4984-ae95-dee9d89d9097', 'hjdkldllskdl'])
        self.assertEqual(resolve(url).func, password_reset_confirm)

    def test_url_PasswordResetDoneView(self):
        url = reverse('users:password_reset_done')
        self.assertEqual(resolve(url).func.view_class,
                         auth_views.PasswordResetDoneView)

    def test_url_password_reset_complete(self):
        url = reverse('users:password_reset_complete')
        self.assertEqual(resolve(url).func.view_class,
                         auth_views.PasswordResetCompleteView)
