# Generated by Django 4.2.10 on 2024-03-19 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_news_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_count',
        ),
    ]
