# Generated by Django 3.2.8 on 2021-12-22 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autopart',
            name='price',
            field=models.BigIntegerField(default=1200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carApp.car'),
        ),
    ]
