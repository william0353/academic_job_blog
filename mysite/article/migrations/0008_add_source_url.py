# Generated by Django 3.0.5 on 2020-09-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_add_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_source',
            name='url',
            field=models.URLField(null=True),
        ),
    ]