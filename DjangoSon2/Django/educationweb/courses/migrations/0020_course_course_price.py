# Generated by Django 3.2.12 on 2022-12-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20221209_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.CharField(default='Free', max_length=10),
        ),
    ]
