# Generated by Django 3.2.7 on 2021-11-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210930_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=160),
        ),
    ]