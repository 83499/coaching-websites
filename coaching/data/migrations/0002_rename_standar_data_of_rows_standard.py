# Generated by Django 3.2.2 on 2021-05-13 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_of_rows',
            old_name='standar',
            new_name='standard',
        ),
    ]
