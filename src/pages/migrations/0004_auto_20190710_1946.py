# Generated by Django 2.1.9 on 2019-07-10 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='user_id',
            new_name='user',
        ),
    ]