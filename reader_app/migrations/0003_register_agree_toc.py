# Generated by Django 2.1 on 2019-08-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader_app', '0002_auto_20190822_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Agree_Toc',
            field=models.BooleanField(default=True),
        ),
    ]
