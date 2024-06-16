# Generated by Django 5.0.1 on 2024-03-05 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phoneno', models.BigIntegerField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customerproductorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.TextField(max_length=100)),
                ('contactno', models.BigIntegerField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('keyuser', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='customermachineryorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcategory', models.CharField(choices=[('tool', 'Machinery'), ('pesticide', 'Pesticide')], default='tool', max_length=50)),
                ('quantity', models.FloatField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('contactno', models.BigIntegerField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmadmin.customerdetails')),
            ],
        ),
    ]