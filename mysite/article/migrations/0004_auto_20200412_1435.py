# Generated by Django 3.0.4 on 2020-04-12 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_create_time_roll'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_time_roll']},
        ),
    ]
