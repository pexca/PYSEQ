# Generated by Django 2.2.11 on 2020-03-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20200321_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]