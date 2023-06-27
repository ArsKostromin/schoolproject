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
        
    def test_urls_uses_correct_template(self) -> None:
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names: dict = {
            reverse('index'): 'app_news/aboutUs.html',
        }
        for adress, template in templates_url_names.items():
            with self.subTest(adress = adress):
                response = self.guest_client.get(adress)
                error_name: str = f'Ошибка: {adress} ожидал шаблон {template}'
                self.assertTemplateUsed(response, template, error_name)
                
    

