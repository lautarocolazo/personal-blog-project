# Generated by Django 3.2.5 on 2021-07-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Here goes your post snippet', max_length=200),
        ),
    ]
