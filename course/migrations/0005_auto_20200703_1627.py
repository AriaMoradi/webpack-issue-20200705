# Generated by Django 3.0.7 on 2020-07-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200703_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
