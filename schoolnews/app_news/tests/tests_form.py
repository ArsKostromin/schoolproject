from django.test import TestCase, Client
from app_news.models import Comment, Product, Rubric
from schoolnews import settings
from django.contrib.auth  import get_user_model
from users.models import MyUser 
from django.urls import reverse
from http import HTTPStatus


# Create your tests here.

User = get_user_model()

class CommentFormTests(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='auth1', password='1X<ISRUkw+tuK')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.rubric = Rubric.objects.create(name='1test_rubric')
        self.product = Product.objects.create(title='1тест_имя',content='1test_content', rubric=Rubric.objects.get(id=1),)
        self.comment = Comment.objects.create(user=self.user, product=self.product, body='1test_text')


    def test_create_comment(self):
        '''Проверка создания поста'''
        comment_count = Comment.objects.count()
        form_data ={'body':'Текст записанный в форму',
                    'product':self.product.id}
        response = self.authorized_client.post(reverse('detail_product', kwargs={'pk': self.product.id}),
        data=form_data,
        follow = True)
        error_name1 = 'Данные поста не совпадают'
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(Comment.objects.filter(body='Текст записанный в форму',
        product=self.product.id,
        user=self.user
        ).exists(), error_name1)
        error_name2 = 'Пост не добавлен в базу данных'
        self.assertEqual(Comment.objects.count(),
                        comment_count + 1, error_name2)


    '''    def test_reddirect_guest_client(self):
        
        self.comment = Comment.objects.create(body='Тестовый текст',
                                        user=self.user,
                                        product=self.product)
        form_data = {'body': 'Текст записанный в форму'}
        response = self.guest_client.post(reverse('detail_product', kwargs={'pk': self.product.id}),
            data=form_data,
            follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response,
                             f'/auth/login/?next=/{self.product.id}')

'''