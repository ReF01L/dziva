# Generated by Django 3.1.5 on 2021-01-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productmethods'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='structure',
            field=models.CharField(blank=True, max_length=200, verbose_name='Состав'),
        ),
    ]
