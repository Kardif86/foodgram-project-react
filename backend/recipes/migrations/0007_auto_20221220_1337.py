# Generated by Django 2.2.19 on 2022-12-20 10:37

from django.db import migrations

import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20221220_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=7, samples=None, unique=True),
        ),
    ]
