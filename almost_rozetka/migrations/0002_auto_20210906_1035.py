# Generated by Django 3.2.6 on 2021-09-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almost_rozetka', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='product',
            field=models.ManyToManyField(blank=True, to='almost_rozetka.Product'),
        ),
    ]