# Generated by Django 4.1.2 on 2022-10-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donasi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donasi',
            name='target',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
