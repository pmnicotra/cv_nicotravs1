# Generated by Django 4.0.5 on 2022-07-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0003_delete_logros_rename_tareas_1_experiencia_tareas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='desde',
            field=models.CharField(max_length=50),
        ),
    ]