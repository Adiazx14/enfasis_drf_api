# Generated by Django 3.2.7 on 2021-09-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='revista',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
