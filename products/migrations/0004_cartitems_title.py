# Generated by Django 3.0.4 on 2020-04-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
