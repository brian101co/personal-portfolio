# Generated by Django 3.0.7 on 2020-07-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_job_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='code_url',
            field=models.CharField(default='null', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='site_url',
            field=models.CharField(default='null', max_length=150),
            preserve_default=False,
        ),
    ]
