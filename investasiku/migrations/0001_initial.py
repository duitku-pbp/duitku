# Generated by Django 4.1.2 on 2022-10-27 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_name', models.CharField(max_length=64)),
                ('investment_type', models.CharField(max_length=64)),
                ('cagr_1Y', models.DecimalField(decimal_places=2, max_digits=6)),
                ('drawdown_1Y', models.DecimalField(decimal_places=2, max_digits=6)),
                ('aum', models.CharField(max_length=64)),
                ('expense_ratio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('min_buy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Portofolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_value', models.IntegerField()),
                ('investment', models.ManyToManyField(to='investasiku.investment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
