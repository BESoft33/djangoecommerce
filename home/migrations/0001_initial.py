# Generated by Django 3.1.7 on 2021-05-07 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('status', models.CharField(choices=[('active', 'Available'), ('inactive', 'Unavailable')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'Available'), ('inactive', 'Unavailable')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'Available'), ('inactive', 'Unavailable')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField(default=0)),
                ('label', models.CharField(blank=True, choices=[('new', 'New'), ('hot', 'hot')], max_length=200)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'Available'), ('inactive', 'Unavailable')], max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(max_length=200)),
                ('specification', models.TextField(blank=True)),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
