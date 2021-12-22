# Generated by Django 3.2.9 on 2021-12-22 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPart',
            fields=[
                ('part_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Something', max_length=50)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=70)),
                ('startDate', models.DateField(auto_now=True)),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('price', models.BigIntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.BigIntegerField()),
                ('order_date', models.DateField(auto_now=True)),
                ('delivery_date', models.DateField()),
                ('delivery_address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.order')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.autopart')),
            ],
        ),
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.TextField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.autopart')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.car')),
            ],
        ),
        migrations.AddField(
            model_name='autopart',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.car'),
        ),
        migrations.AddField(
            model_name='autopart',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carApp.partcategory'),
        ),
    ]
