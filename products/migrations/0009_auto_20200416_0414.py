# Generated by Django 3.0.4 on 2020-04-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200416_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='slug',
            field=models.SlugField(default='no-slug', max_length=100, unique=True),
        ),
    ]
