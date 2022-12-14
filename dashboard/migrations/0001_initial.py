# Generated by Django 3.2.15 on 2022-10-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('work_contents', models.CharField(max_length=255)),
                ('wow_point', models.CharField(max_length=255)),
                ('seeds_of_growth', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
