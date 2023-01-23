from django.db import models
from django.contrib.auth.models import User
from schoolnews import settings
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=35, verbose_name='Заголовок')
    content=models.TextField(null=True, blank=True, verbose_name='содержание')#null=True и blank=True делаю поле необязательным к заполнению
    published=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')#при выводе объявлений мы будем сортировать их по убыванию даты публикации,и индекс здесь очень пригодится.
    img=models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Картика')
    slug = models.SlugField(max_length=200, null=True, blank=True, db_index=True)
    rubric=models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


    class Meta:#отображение в панели администратора
        verbose_name_plural='Новости' 
        verbose_name='Новость'
        ordering = ['-published']#сортировка по убыванию публикаций 

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('detail_product', args=[str(self.id)])

    def __str__(self):# Строка для представления объекта Model.
        return self.title

class Rubric(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Рубрики'
        verbose_name='Рубрика'
        ordering=['name']#сортировка по имени 

    def get_absolute_url(self):
        return reverse('rubric_detail', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    reply = models.ForeignKey('self',related_name="replies", on_delete = models.CASCADE , blank= True ,null=True, verbose_name='ответ')
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE, verbose_name='новость')
    body = models.TextField(max_length=120, verbose_name='комментарий', help_text='Введите текст комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.product)

    class Meta:
        verbose_name_plural='Комментарий'
        verbose_name = 'комментарий'
        ordering = ('created',)

   