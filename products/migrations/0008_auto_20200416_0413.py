# Generated by Django 3.0.4 on 2020-04-15 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200416_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]
