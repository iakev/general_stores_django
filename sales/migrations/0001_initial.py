# Generated by Django 3.2.10 on 2022-01-06 08:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_paid', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('tax_amount', models.IntegerField(null=True)),
                ('sales_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.salesstatus')),
            ],
            options={
                'verbose_name_plural': 'Sales',
            },
        ),
    ]
