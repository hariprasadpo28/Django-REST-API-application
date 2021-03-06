# Generated by Django 3.2.1 on 2021-05-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_name', models.CharField(max_length=50)),
                ('photo_url', models.CharField(max_length=150)),
                ('advisor_id', models.IntegerField()),
                ('booking_time', models.DateTimeField()),
                ('user', models.IntegerField()),
            ],
        ),
    ]
