# Generated by Django 4.0.4 on 2022-04-20 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_positive', models.IntegerField()),
                ('number_of_recoverd', models.IntegerField()),
                ('number_of_negative', models.IntegerField()),
                ('date', models.DateField()),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions_api.region')),
            ],
        ),
    ]
