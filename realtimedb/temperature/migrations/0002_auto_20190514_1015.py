# Generated by Django 3.0.dev20190513194854 on 2019-05-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
