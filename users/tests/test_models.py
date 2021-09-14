from django.test import TestCase
from ..models import User, passwordresetcode


""" The tests here are to ensure the right flow of models creation in the database """


class ModelsTests(TestCase):

    def setUp(self):
        # create a test user
        self.user = User.objects.create(
            email="example@mail.com", password="sola@12345")
        self.passwordresetcode_create = passwordresetcode.objects.create(
            code="djdieue78994m", user=self.user)

    # count the users available
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    # Fetch the user with an email
    def test_user_exist(self):
        qs = User.objects.filter(email="example@mail.com")
        self.assertTrue(qs.exists())

    def test_passwordresetcode_exist(self):
        code = "djdieue78994m"
        qs = passwordresetcode.objects.filter(user=self.user, code=code)
        self.assertTrue(qs.exists())
