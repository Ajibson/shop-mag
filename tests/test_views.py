from django.test import TestCase, Client
from django.urls import reverse


class ViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse("index")
        self.signup_url = reverse('users:signup')
        self.login_url = reverse('users:login')
        self.logout_url = reverse('users:logout')
        self.reset_password_url = reverse('users:reset_password')
        self.password_reset_done_url = reverse("users:password_reset_done")
        self.password_reset_complete_url = reverse(
            "users:password_reset_complete")

    def test_index_temmplate(self):
        response = self.client.get(self.home_url)
        # self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_signup_template(self):
        response = self.client.get(self.signup_url)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_login_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_template(self):
        response = self.client.get(self.logout_url)
        # This is to test if the redirection actually take place
        self.assertEqual(response.status_code, 302)
        # This will test to ensure that no template is uses for logout
        # self.assertTemplateUsed(response, '')

    def test_reset_password_template(self):
        response = self.client.get(self.reset_password_url)
        self.assertTemplateUsed(response, 'users/password_reset_form.html')

    def test_password_reset_done_template(self):
        response = self.client.get(self.password_reset_done_url)
        self.assertTemplateUsed(response, 'users/password_reset_done.html')

    def test_password_reset_complete_template(self):
        response = self.client.get(self.password_reset_complete_url)
        self.assertTemplateUsed(response, 'users/password_reset_complete.html')
