# Generated by Django 3.1.3 on 2021-02-16 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hot_res_app', '0011_completed_order_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaiterCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=31)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=31),
        ),
    ]
