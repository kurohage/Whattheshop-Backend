# Generated by Django 2.2.7 on 2019-12-02 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191201_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
