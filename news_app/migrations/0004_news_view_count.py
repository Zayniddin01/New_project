# Generated by Django 4.2.10 on 2024-03-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
