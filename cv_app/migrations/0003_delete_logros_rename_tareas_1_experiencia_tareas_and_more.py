# Generated by Django 4.0.5 on 2022-07-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0002_logros_skills'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logros',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='tareas_1',
            new_name='tareas',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='tareas_2',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='tareas_3',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='tareas_4',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='tareas_5',
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='desde',
            field=models.DateField(),
        ),
    ]