# Generated by Django 3.0.7 on 2020-08-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20200720_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='reviewer',
            field=models.CharField(default='reviewer', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='testimonial',
            field=models.TextField(blank=True),
        ),
    ]