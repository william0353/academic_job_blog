# Generated by Django 3.0.5 on 2020-08-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_email_reminder_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='pay_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='email_reminder',
            name='frequency',
            field=models.CharField(choices=[('per month', 'Per Month'), ('per week', 'Per Week'), ('per day', 'Per Day'), ('immediately', 'Fastest'), ('wrong', 'wrong reminder')], default='per month', max_length=15),
        ),
        migrations.AlterField(
            model_name='email_reminder',
            name='key_word',
            field=models.CharField(max_length=200, null=True),
        ),
    ]