from django.test import TestCase
from images.models import Image, Category
from users.models import User


""" The tests here are to ensure the right flow of models creation in the database """


class ModelsTests(TestCase):

    def setUp(self):
        # create a test user
        self.user = User.objects.create(
            email="example@mail.com", password="sola@12345")
        self.category_obj = Category.objects.create(name="programming")
        self.image_obj = Image.objects.create(
            user=self.user, price=20, image_category=self.category_obj)

    # count the images available
    def test_image_count(self):
        qs = Image.objects.all()
        self.assertEqual(qs.count(), 1)

    # Test if image exist after creation
    def test_image_exist(self):
        qs = Image.objects.filter(user=self.user)
        self.assertTrue(qs.exists())

    # confirm the category the created image fall into
    def test_image_category(self):
        qs = Image.objects.filter(image_category=self.category_obj)
        self.assertTrue(qs.exists())

    
