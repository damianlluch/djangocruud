# Generated by Django 2.2.2 on 2019-07-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_fbv_user', '0004_auto_20190727_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
    ]