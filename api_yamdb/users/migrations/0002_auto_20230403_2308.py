# Generated by Django 3.2 on 2023-04-03 20:08

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', error_messages={'validators': 'Выбрана несуществующая роль'}, max_length=16, verbose_name='Пользовательская роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем пользователя уже существует.'}, max_length=150, unique=True, validators=[users.validators.CustomUsernameValidator(), users.validators.username_me], verbose_name='username'),
        ),
    ]
