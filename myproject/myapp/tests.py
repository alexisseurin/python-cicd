from django.test import TestCase
from django.urls import reverse

class HelloViewTests(TestCase):
    def test_hello_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world!")
