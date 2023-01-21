from django.test import TestCase
from app_news.models import Comment, Product, Rubric
from schoolnews import settings
from django.contrib.auth  import get_user_model
from users.models import MyUser 

# Create your tests here.

class productModelTest(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user= MyUser.objects.create_user(username='auth', password='0X<ISRUkw+tuK')
        self.rubric = Rubric.objects.create(name='test_rubric')
        self.product = Product.objects.create(title='тест_имя',content='test_content', rubric=Rubric.objects.get(id=1),)
        self.comment = Comment.objects.create(user=self.user, product=self.product, body='test_text')

    def test_title(self):
        '''Проверка заполнения verbose_name'''
        field_verboses={'title': 'Заголовок',
                        'content': 'содержание',
                        'published': 'Опубликовано',
                        'img': 'Картика',
                        'rubric': 'Рубрика',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.product._meta.get_field(field).verbose_name,
                    expected_value, error_name)


    def test_help_text_in_comment(self):
        '''проверка заполнения help_text'''
        fields_help_text = {
            'body': 'Введите текст комментария',
        }
        for field, expected_value in fields_help_text.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.comment._meta.get_field(field).help_text, expected_value, error_name
                )

