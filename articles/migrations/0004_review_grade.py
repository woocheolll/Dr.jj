# Generated by Django 3.2.13 on 2022-11-02 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20221102_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
