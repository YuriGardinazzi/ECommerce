from django.test import TestCase
from django.urls import reverse_lazy

from user_management.models import CustomUser
# Create your tests here.
class TestSignUpView(TestCase):

    def setUp(self):
        email = "prova@email.com"
        username = "prova91"
        first_name = "pino"
        last_name = "pinotto"
        password = "rootroot"

        self.u = CustomUser.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)

    def login_user(self):
        self.client.login(email='prova@email.com', password="rootroot")


    def test_login_redirect(self):
        self.login_user()
        response = self.client.get(reverse_lazy('user_management:login'))
        self.assertEqual(response.status_code, 200, "Authenticated user should return 200")

    def test_products_page_access_without_login(self):
        response = self.client.get(reverse_lazy('product_management:product_management'))
        self.assertEqual(response.status_code,302,"If not authenticated should be redirected")

    def test_products_page_access_with_login(self):
        self.login_user()
        response = self.client.get(reverse_lazy('product_management:product_management'))
        self.assertEqual(response.status_code,200,"user should be logged in")