# Generated by Django 3.2.5 on 2021-07-16 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210716_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='udpated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
