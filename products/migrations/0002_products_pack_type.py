# Generated by Django 3.2.10 on 2022-01-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pack_type',
            field=models.CharField(default='pieces', max_length=255),
            preserve_default=False,
        ),
    ]
