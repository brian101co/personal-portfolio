# Generated by Django 3.0.7 on 2020-07-03 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200630_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='body',
            field=models.TextField(default='fill'),
            preserve_default=False,
        ),
    ]
