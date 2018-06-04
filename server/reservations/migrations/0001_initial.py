# Generated by Django 2.0.2 on 2018-05-19 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=15)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('premise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_premise', to='restaurant.MasterPremise')),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerAnalytics',
            fields=[
                ('analytics_id', models.AutoField(primary_key=True, serialize=False)),
                ('analytics_attribute', models.CharField(blank=True, max_length=50, null=True)),
                ('attribute_value', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_analytics', to='reservations.Customer')),
                ('premise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='premise_analytics', to='restaurant.MasterPremise')),
            ],
            options={
                'verbose_name_plural': 'Customer Analytics',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('customer_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_attribute', models.CharField(blank=True, max_length=50, null=True)),
                ('attribute_value', models.CharField(blank=True, max_length=50, null=True)),
                ('attribute_status', models.CharField(blank=True, max_length=10, null=True)),
                ('last_update_date', models.DateTimeField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_details', to='reservations.Customer')),
            ],
            options={
                'verbose_name_plural': 'Customer Details',
            },
        ),
        migrations.CreateModel(
            name='MasterTable',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=100)),
                ('table_type', models.CharField(max_length=100)),
                ('premise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_premise', to='restaurant.MasterPremise')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_section', to='restaurant.PremiseSections')),
            ],
            options={
                'verbose_name_plural': 'Master Tables ',
            },
        ),
        migrations.CreateModel(
            name='ReservationQueue',
            fields=[
                ('reservation_queue_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_status', models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Waiting', 'Waiting'), ('Canceled', 'Canceled'), ('Cleaning', 'Cleaning')], default='Available', max_length=10)),
                ('reservation_for_date', models.DateField()),
                ('reservation_start_time', models.TimeField()),
                ('pax', models.IntegerField(blank=True, null=True)),
                ('reservation_date', models.DateTimeField(blank=True, null=True)),
                ('reservation_type', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_in_queue', to='reservations.Customer')),
                ('premise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_premise', to='restaurant.MasterPremise')),
                ('reserved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserved_by', to=settings.AUTH_USER_MODEL)),
                ('seating_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pref_section', to='restaurant.PremiseSections')),
                ('table_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reserved_table', to='reservations.MasterTable')),
            ],
            options={
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='TableAttributes',
            fields=[
                ('table_attribute_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_attribute_value', models.CharField(max_length=100)),
                ('table_status', models.CharField(max_length=50)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_attributes', to='reservations.MasterTable')),
            ],
            options={
                'verbose_name_plural': 'Table Attributes',
            },
        ),
        migrations.CreateModel(
            name='TableAvailability',
            fields=[
                ('tbl_availability_id', models.AutoField(primary_key=True, serialize=False)),
                ('tbl_availability_date', models.DateField()),
                ('tbl_availability_status', models.CharField(max_length=15)),
                ('tbl_availability_start_time', models.TimeField()),
                ('tbl_availability_end_time', models.TimeField()),
                ('table_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_table', to='reservations.MasterTable')),
            ],
            options={
                'verbose_name_plural': 'Table Availability',
            },
        ),
    ]
