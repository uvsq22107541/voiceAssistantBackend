# Generated by Django 3.1 on 2020-10-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='level',
            field=models.IntegerField(default=2),
        ),
    ]
