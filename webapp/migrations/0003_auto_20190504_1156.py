# Generated by Django 2.1.7 on 2019-05-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190504_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
    ]
