# Generated by Django 2.0.7 on 2022-05-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='summery',
            field=models.TextField(default='Il est default value'),
        ),
    ]
