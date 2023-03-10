# Generated by Django 3.2 on 2022-12-28 10:56

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('mobile_no', models.CharField(max_length=10, unique=True, validators=[main.models.mobile_validate])),
                ('resume', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Client_testonomial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_message', models.CharField(max_length=500)),
                ('client_image', models.ImageField(upload_to='client_image')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10, validators=[main.models.mobile_validate])),
                ('message', models.TextField()),
            ],
        ),
    ]
