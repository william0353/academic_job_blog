# Generated by Django 3.0.4 on 2020-04-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200326_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_time_roll',
            field=models.DateTimeField(auto_now=True),
        ),
    ]