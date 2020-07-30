# Generated by Django 3.0.7 on 2020-07-23 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=15)),
                ('message', models.CharField(max_length=500)),
                ('from_email', models.EmailField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_donor', models.BooleanField(default=False)),
                ('is_volunteer', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=250)),
                ('email_address', models.CharField(max_length=30)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('address', models.ManyToManyField(to='members.Address')),
                ('membership', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.Membership')),
            ],
        ),
    ]
