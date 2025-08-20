from django.test import TestCase
from .models import User,Order
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class TestUserOrder(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        user1= User.objects.create(username='testuser1')
        user1.set_password('password123')
        user1.save()
        user2 = User.objects.create(username='testuser2')
        user2.set_password('password456')
        user2.save()
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)

    def test_user_order_auth(self):
        user=User.objects.get(username='testuser1')
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(reverse('uo'))
        data=response.json()
        print(data)
        assert response.status_code == status.HTTP_200_OK

    def test_user_order_unauth(self):
        response = self.client.get(reverse('uo'))
        assert response.status_code == status.HTTP_403_FORBIDDEN



