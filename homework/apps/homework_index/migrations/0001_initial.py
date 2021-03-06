# Generated by Django 3.0 on 2020-01-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_author', models.CharField(default='', max_length=50, verbose_name='Автор')),
                ('homework_lesson', models.CharField(max_length=100, verbose_name='Название урока')),
                ('homework', models.TextField(verbose_name='Задание')),
                ('use_date', models.DateField(default='', null=True, verbose_name='Дата урока')),
                ('date_for_server', models.TextField(default='', null=True, verbose_name='Дата урока')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
