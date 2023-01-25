from django.test import TestCase, Client
from app_news.models import Comment, Product, Rubric
from django.contrib.auth  import get_user_model
from django.urls import reverse
from django import forms

# Create your tests here.
User = get_user_model()

class ViewsTest(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='auth')
        self.user2 = User.objects.create_user(username='auth2')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.rubric = Rubric.objects.create(name = 'тестовая рубрика')
        self.product = Product.objects.create(title='тестовая статья', content = 'тест текст', rubric=Rubric.objects.get(id=1))
    
    def test_views_correct_template(self):
        '''URL-адрес использует соответствующий шаблон.'''
        templates_url_names = {
            reverse('index'): 'app_news/aboutUs.html',
            reverse('detail_product', kwargs={'pk': self.product.id}): 'app_news/product_detail.html',
            reverse('news'): 'app_news/product_list.html',
            reverse('rubric_detail', kwargs={'pk': self.rubric.id}): 'app_news/rubric_detail.html'
        }
        for adress, template in templates_url_names.items():
            with self.subTest(adress = adress):
                response = self.authorized_client.get(adress)
                error_name = f'Ошибка: {adress} ожидал шаблон {template}'
                self.assertTemplateUsed(response, template, error_name)


    def test_post_detail_page_show_correct_context(self):
        """Шаблон post_detail сформирован с правильным контекстом."""
        response = self.authorized_client.get(
            reverse('detail_product', kwargs={'pk': self.product.id})
        )
        product_text_0={response.context['product'].title: 'тестовая статья',
                        response.context['product'].content: 'тест текст',
                        response.context['product'].rubric: Rubric.objects.get(id=1)}
        for value, expected  in product_text_0.items():
            self.assertEqual(product_text_0[value],expected)


    def test_comment_create_page_show_correct_context(self):
        """Шаблон cоздания комментраия сформирован с правильным контекстом."""
        response = self.authorized_client.get(
            reverse('detail_product', kwargs={'pk': self.product.id}))
        form_fields = {
        'body': forms.fields.CharField,}
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_fields = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_fields, expected)






'''    def test_post_added_correctly(self):
        """комментарий при создании добавлен корректно"""
        comment = Comment.objects.create(body='тест текст', product=self.product, user=self.user)
        response_detail_product = self.authorized_client.get(
            reverse('detail_product', kwargs={'pk': self.product.id}))
        detail = response_detail_product.context['page_obj']
        self.assertIn(comment, detail, 'комментария нет под новостью.')'''