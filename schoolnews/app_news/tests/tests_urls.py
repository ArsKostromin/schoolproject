from http import HTTPStatus
from django.test import Client, TestCase
from django.urls import reverse

class StaticurlTests(TestCase):

    def setUp(self) -> None:
        self.guest_client = Client()

    def test_static_page(self) -> None:
        """Страница доступка по URL."""
        pages: tuple = (reverse('index'),)
        for page in pages:
            response = self.guest_client.get(page)
            error_name: str =f'Ошибка: нед доступа страницы {page}'
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)
        
    
