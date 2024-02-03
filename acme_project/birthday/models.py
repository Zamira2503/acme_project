# birthday/models.py
from django.db import models

# Импортируется функция-валидатор.
from .validators import real_age

# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

from django.contrib.auth import get_user_model

# Да, именно так всегда и ссылаемся на модель пользователя!
User = get_user_model()


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    ) 
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    # В моделях Django есть специальный тип поля, 
    # предназначенный для изображений:  models.ImageField()
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
    
    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
