# Generated by Django 3.2.5 on 2021-07-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=50)),
                ('empname', models.CharField(max_length=50)),
                ('empsal', models.FloatField()),
                ('empaddr', models.TextField(max_length=250)),
            ],
        ),
    ]
