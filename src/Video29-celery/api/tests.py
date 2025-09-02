from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User,Product

class ProductTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin','123456')
        self.user = User.objects.create_user('user','123456')
        self.product = Product.objects.create(
            name="Test Product",
            price=9.99,
            stock=5,
        )
        self.url=reverse('product-detail',kwargs={'product_id':self.product.id})
    def test_product_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['id'], self.product.id)
        self.assertEqual(float(response.data['price']), self.product.price)
        self.assertEqual(response.data['stock'], self.product.stock)

    def test_unauthorized_product_add(self):
        data = {
            "name": "New Product",
            "price": 19.99,
            "stock": 10
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 401)

