# Generated by Django 2.2.7 on 2019-12-10 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
    ]
