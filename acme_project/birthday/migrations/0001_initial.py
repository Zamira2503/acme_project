# Generated by Django 5.0.1 on 2024-01-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Необязательное поле', max_length=20, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
    ]
