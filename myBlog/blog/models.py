from django.db import models

# Create your models here.

class Post(models.Model):
    """Post data"""
    title = models.CharField('Заголовок записи', max_length=200)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор записи', max_length=100)
    date = models.DateField('Дата публикации записи')
    img = models.ImageField('Изображения', upload_to='image/%Y')
    
    def __str__(self):
        return f'{self.title}, {self.author}'
    
    class Meta():
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        
    
    
    
    