# Generated by Django 5.0.3 on 2024-03-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderPizza', '0005_dailymenu_pizza_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymenu',
            name='pizza_type',
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_type',
            field=models.CharField(choices=[('Happy', 'Happy Pizza'), ('Joshua', 'Joshua Pizza')], default='Happy', max_length=6),
        ),
    ]
