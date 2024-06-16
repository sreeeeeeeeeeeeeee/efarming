# Generated by Django 5.0.1 on 2024-03-05 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmer', '0001_initial'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendrentrequest',
            name='toolid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.renttools'),
        ),
        migrations.AddField(
            model_name='sendtoolorderrequest',
            name='toolid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellingproducts'),
        ),
    ]