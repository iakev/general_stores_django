# Generated by Django 3.2.10 on 2022-01-04 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_pack_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('-date_added',), 'verbose_name_plural': 'Products'},
        ),
    ]
