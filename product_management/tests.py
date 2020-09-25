from django.test import TestCase

from .models import Review, Product
from user_management.models import CustomUser
# Create your tests here.
class TestReview(TestCase):
    def setUp(self):
        email = "prova@email.com"
        username = "prova91"
        first_name = "pino"
        last_name = "pinotto"
        password = "rootroot"
        is_vendor = True

        self.u = CustomUser.objects.create_user(email=email, username=username, first_name=first_name,
                                                last_name=last_name, password=password)
        self.p = Product.objects.create()