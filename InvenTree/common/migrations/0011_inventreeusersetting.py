# Generated by Django 3.2.4 on 2021-07-19 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0010_migrate_currency_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvenTreeUserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='Settings key (must be unique - case insensitive', max_length=50, unique=True)),
                ('value', models.CharField(blank=True, help_text='Settings value', max_length=200)),
                ('user', models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'InvenTree User Setting',
                'verbose_name_plural': 'InvenTree User Settings',
            },
        ),
    ]
