# Generated by Django 4.1.2 on 2022-10-11 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Specialty', models.CharField(max_length=40)),
                ('Reg_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Sex', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('ContactNo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_time', models.DateTimeField()),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_chan.patient')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_chan.doctor')),
            ],
        ),
    ]
