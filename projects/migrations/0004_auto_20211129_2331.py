# Generated by Django 3.2.4 on 2021-11-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20211129_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='practice',
        ),
        migrations.AlterField(
            model_name='job',
            name='reviewer',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]