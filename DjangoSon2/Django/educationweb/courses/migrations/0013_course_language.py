# Generated by Django 3.2.12 on 2022-12-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20221205_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Language',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
