# Generated by Django 2.2.4 on 2023-01-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views'),
        ),
    ]
