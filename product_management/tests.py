from django.test import TestCase
from django.urls import reverse_lazy

from .models import Review, Product, MyCategory
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
        self.c = MyCategory.objects.create(name='usato', description='blablabla')

        self.p = Product.objects.create(name='prodotto', description='qualcosa', price=100, quantity=10,
                                        category_id=self.c.name, producer_id=self.u.id)

    def login_user(self):
        self.client.login(email="prova@email.com", passwrod="rootroot")

    def test_add_review_negative_rating(self):
        self.login_user()
        data = {
            'type':'POST',
            'product_id': self.p.id,
            'review': 'blablabla',
            'rating': -10,
            'user_id': self.u.id
        }
        response = self.client.post(reverse_lazy('product_management:add_review'),data)
        self.assertEqual(response.status_code,403,'Show 403 if rating is < 0')

    def test_add_review_with_too_high_rating(self):
        self.login_user()
        data = {
            'type':'POST',
            'product_id': self.p.id,
            'review': 'blablabla',
            'rating': 6,
            'user_id': self.u.id
        }
        response = self.client.post(reverse_lazy('product_management:add_review'),data)
        self.assertEqual(response.status_code,403,'Show 403 if rating is > 5')

    def test_add_correct_review(self):
        self.login_user()
        data = {
            'type':'POST',
            'product_id': self.p.id,
            'review': 'blablabla',
            'rating': 3,
            'user_id': self.u.id
        }
        response = self.client.post(reverse_lazy('product_management:add_review'),data)
        self.assertEqual(response.status_code,200,'200 if review is correct')