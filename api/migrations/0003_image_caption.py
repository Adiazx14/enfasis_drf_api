# Generated by Django 3.2.7 on 2021-09-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210914_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
