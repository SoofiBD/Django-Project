# Generated by Django 3.2.12 on 2022-12-06 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('courses', '0013_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Language',
            field=models.CharField(default='English', max_length=30),
        ),
    ]
