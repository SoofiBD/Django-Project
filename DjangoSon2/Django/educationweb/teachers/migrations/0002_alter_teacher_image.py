# Generated by Django 3.2.12 on 2022-12-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, default='courses/static/img/courses-1.jpg', upload_to='courses\\%Y\\%m\\%d'),
        ),
    ]
