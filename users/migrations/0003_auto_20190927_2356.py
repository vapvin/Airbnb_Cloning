# Generated by Django 2.2.5 on 2019-09-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190925_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='langauge',
            new_name='language',
        ),
    ]
