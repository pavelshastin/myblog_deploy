# Generated by Django 2.1.7 on 2019-03-21 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]