# Generated by Django 4.1.7 on 2023-03-14 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='views',
            new_name='view',
        ),
    ]