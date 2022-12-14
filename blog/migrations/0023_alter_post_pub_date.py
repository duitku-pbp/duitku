# Generated by Django 4.1.2 on 2022-10-14 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0022_alter_post_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 10, 14, 10, 36, 27, 348540, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date published",
            ),
        ),
    ]
