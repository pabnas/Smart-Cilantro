# Generated by Django 2.1.7 on 2019-02-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('humedad', models.FloatField()),
                ('temperatura', models.FloatField()),
            ],
        ),
    ]
