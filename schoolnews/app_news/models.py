from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=35, verbose_name='Заголовок')
    content=models.TextField(null=True, blank=True, verbose_name='содержание')#null=True и blank=True делаю поле необязательным к заполнению
    published=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')#при выводе объявлений мы будем сортировать их по убыванию даты публикации,и индекс здесь очень пригодится.
    img=models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Картика')
    rubric=models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


    class Meta:#отображение в панели администратора
        verbose_name_plural='Новости' 
        verbose_name='Новость'
        ordering = ['-published']#сортировка по убыванию публикаций 



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

class comment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments')
    body = models.TextField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)

    class Meta:
        ordering = ('created',)

    