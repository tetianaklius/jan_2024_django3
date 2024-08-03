# Generated by Django 5.0.7 on 2024-08-02 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0004_carmodel_body_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
            preserve_default=False,
        ),
    ]
