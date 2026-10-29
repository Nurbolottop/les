from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название сайта')
    description = models.TextField(verbose_name='Описание сайта')
    logo = models.ImageField(upload_to='logos/', verbose_name='Логотип',blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

