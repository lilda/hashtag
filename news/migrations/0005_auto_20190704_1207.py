# Generated by Django 2.1.8 on 2019-07-04 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190704_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag',
        ),
    ]
