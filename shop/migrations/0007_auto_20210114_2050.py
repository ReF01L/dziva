# Generated by Django 3.1.5 on 2021-01-14 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210114_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcharacters',
            options={'verbose_name': 'Характеристика продукта', 'verbose_name_plural': 'Характеристики продукта'},
        ),
        migrations.AlterModelOptions(
            name='productmethods',
            options={'verbose_name': 'Способ употребления', 'verbose_name_plural': 'Способы употребления'},
        ),
    ]