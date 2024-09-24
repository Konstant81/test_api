# Generated by Django 4.2.15 on 2024-09-24 10:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(message='Введите телефон в формате 7ХХХХХХХХХХ', regex='^7\\d{10}$')])),
                ('code', models.CharField(blank=True)),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField()),
                ('text', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, validators=[django.core.validators.MinLengthValidator(limit_value=3), django.core.validators.MaxLengthValidator(limit_value=3)])),
                ('tag', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'db_table': 'send',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sender.client', verbose_name='клиент')),
                ('send_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sender.send', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'db_table': 'message',
            },
        ),
    ]