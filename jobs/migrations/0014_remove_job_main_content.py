# Generated by Django 3.0.7 on 2020-08-23 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20200823_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='main_content',
        ),
    ]