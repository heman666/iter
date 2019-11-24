# Generated by Django 2.2.2 on 2019-07-09 13:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('Bus_type', models.CharField(choices=[('Sleeper', 'Sleeper'), ('Semi Sleeper', 'Semi Sleeper'), ('Seater', 'Seater')], max_length=20)),
                ('Bus_model', models.CharField(choices=[('scania', 'scania'), ('volvo', 'volvo'), ('super luxary', 'super luxary'), ('Normal', 'Normal')], max_length=20, null=True)),
                ('serviceno', models.IntegerField(primary_key=True, serialize=False)),
                ('distance_from_startcity', models.FloatField(default=600)),
                ('costperkm', models.FloatField()),
                ('noseats', models.IntegerField(default=40)),
                ('start_city', models.CharField(max_length=50)),
                ('destination_city', models.CharField(max_length=50)),
                ('seats_available', models.CharField(default='????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????', max_length=1000)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('reach', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField()),
                ('journeytime', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Booking',
            fields=[
                ('bus_type', models.CharField(max_length=20)),
                ('Bus_model', models.CharField(max_length=20, null=True)),
                ('start_city', models.CharField(max_length=50)),
                ('destination_city', models.CharField(max_length=50)),
                ('bus_start_date', models.DateField()),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('reach', models.DateTimeField(blank=True, null=True)),
                ('booking_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fare', models.FloatField(default='1000.0')),
                ('email', models.EmailField(default='koushiks666@gmail.com', max_length=254)),
                ('phone_number', models.CharField(default='8179033301', max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_cell', message='Enter a valid phone number', regex='^[1-9]{1}[0-9]{9}$')])),
                ('serviceno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='via',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('distance_from_startcity', models.FloatField()),
                ('reach', models.DateTimeField(blank=True, null=True)),
                ('journeytime', models.IntegerField(null=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=6)),
                ('age', models.IntegerField()),
                ('seatno', models.CharField(default=1, max_length=5)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus_Booking')),
            ],
        ),
        migrations.CreateModel(
            name='bus_dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Bus_agency',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_cell', message='Enter a valid phone number', regex='^[1-9]{1}[0-9]{9}$')])),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus_agency'),
        ),
    ]
