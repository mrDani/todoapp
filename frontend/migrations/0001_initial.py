# Generated by Django 3.1.6 on 2022-01-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='displaydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=200)),
                ('Sname', models.CharField(max_length=200)),
            ],
        ),
    ]