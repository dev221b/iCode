# Generated by Django 4.1.7 on 2023-03-24 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilec', '0002_rename_create_on_post_more_created_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_More',
        ),
    ]