# Generated by Django 5.0.3 on 2024-03-26 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('itemID', models.IntegerField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=75)),
                ('Distributer', models.CharField(max_length=75)),
                ('imagepath', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('manufacture', models.CharField(max_length=75)),
                ('lastModifed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=70)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='categories', to='itemlistings.main')),
            ],
        ),
    ]