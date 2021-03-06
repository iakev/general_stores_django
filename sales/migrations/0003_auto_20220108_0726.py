# Generated by Django 3.2.10 on 2022-01-08 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20220108_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sale_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sale_amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='sales.salesstatus'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='tax_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
