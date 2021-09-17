from django.test import TestCase
from images.models import Image, Category
from users.models import User
from payments.models import Payment

""" The tests here are to ensure the right flow of models creation in the database """


class ModelsTests(TestCase):

    def setUp(self):
        # create a test user
        self.user = User.objects.create(
            email="example@mail.com", password="sola@12345")
        self.category_obj = Category.objects.create(name="programming")
        self.image_obj = Image.objects.create(
            user=self.user, price=20, image_category=self.category_obj)
        self.payment_obj = Payment.objects.create(image_for=self.image_obj, reference_id="fabfd1ed-b98b-4174-b181-1f2f60a27d21",
                                                  status="pending")

    def test_payment_count(self):
        qs = Payment.objects.all()
        self.assertEqual(qs.count(), 1)

    # Test if image exist after creation
    def test_payment_exist(self):
        qs = Payment.objects.filter(image_for=self.image_obj)
        self.assertTrue(qs.exists())

    # confirm the category the created image fall into
    def test_payment_image(self):
        qs = Payment.objects.filter(image_for=self.image_obj)
        self.assertTrue(qs.exists())
