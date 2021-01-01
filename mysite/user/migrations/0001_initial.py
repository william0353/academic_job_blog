# Generated by Django 3.0.4 on 2020-03-26 21:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[(0, '男'), (1, '女')], default='男', max_length=32)),
                ('position', models.CharField(choices=[(0, '学生'), (1, '研究员'), (3, '助教'), (4, '讲师'), (5, '教授'), (6, '副教授'), (7, '博士生导师')], default='学生', max_length=32)),
                ('degree', models.CharField(choices=[(0, '专科'), (1, '本科'), (2, '硕士'), (3, '博士'), (4, '其他')], default='专科', max_length=32)),
                ('age', models.CharField(choices=[(0, '50s'), (1, '60s'), (2, '70s'), (3, '80s'), (4, '90s'), (5, '00s'), (6, 'others')], default='50s', max_length=10)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['c_time'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
