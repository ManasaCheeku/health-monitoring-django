# Generated by Django 5.2.1 on 2025-05-28 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('symptoms', models.TextField()),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
