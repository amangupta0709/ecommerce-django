# Generated by Django 3.0.4 on 2020-04-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200416_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100),
        ),
    ]