# Generated by Django 3.2.12 on 2022-12-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20221209_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_price',
            field=models.IntegerField(default='100'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.FloatField(default=''),
        ),
    ]