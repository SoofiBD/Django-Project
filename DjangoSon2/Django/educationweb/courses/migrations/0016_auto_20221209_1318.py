# Generated by Django 3.2.12 on 2022-12-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.IntegerField(default='100'),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.FloatField(default='25'),
        ),
        migrations.AddField(
            model_name='course',
            name='lectures',
            field=models.CharField(default='True', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='skill_level',
            field=models.CharField(default='All Level', max_length=50),
        ),
    ]
