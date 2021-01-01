# Generated by Django 3.0.5 on 2020-06-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200513_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email_reminder',
            name='key_word_1',
        ),
        migrations.RemoveField(
            model_name='email_reminder',
            name='key_word_2',
        ),
        migrations.RemoveField(
            model_name='email_reminder',
            name='key_word_3',
        ),
        migrations.RemoveField(
            model_name='email_reminder',
            name='key_word_4',
        ),
        migrations.RemoveField(
            model_name='email_reminder',
            name='key_word_5',
        ),
        migrations.CreateModel(
            name='key_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('creater', models.ManyToManyField(to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='email_reminder',
            name='key_word',
            field=models.ManyToManyField(to='user.key_word'),
        ),
    ]
