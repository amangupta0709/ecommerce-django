# Generated by Django 3.0.4 on 2020-04-15 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_items_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
