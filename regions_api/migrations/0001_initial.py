# Generated by Django 4.0.4 on 2022-04-19 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(choices=[('ENGLAND', 'ENGLAND'), ('SCOTLAND', 'SCOTLAND'), ('WALES', 'WALES'), ('NORTHERN IRELAND', 'NORTHERN_IRELAND')], max_length=120)),
                ('county_name', models.CharField(choices=[('Cambridgeshire', 'cambrigeshire'), ('Derbyshire', 'derbyshire'), ('Devon', 'devon'), ('East Sussex', 'East_sussex'), ('Essex', 'Essex'), ('Gloucestershire', 'gluchestershire'), ('Hampshire', 'hampshire'), ('Kent', 'krent'), ('Lancashire', 'lancashire'), ('Leicestershire', 'leicestershire')], max_length=120)),
                ('city_town', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('RED', 'RED'), ('AMBER', 'AMBER'), ('GREEN', 'GREEN')], max_length=10, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_positive', models.IntegerField()),
                ('number_of_recoverd', models.IntegerField()),
                ('number_of_negative', models.IntegerField()),
                ('date', models.DateField()),
                ('county_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions_api.region')),
            ],
        ),
    ]