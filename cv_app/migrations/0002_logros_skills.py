# Generated by Django 4.0.5 on 2022-07-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50)),
            ],
        ),
    ]
