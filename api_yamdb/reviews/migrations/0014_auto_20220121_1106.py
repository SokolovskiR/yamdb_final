# Generated by Django 2.2.16 on 2022-01-21 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20220121_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]
