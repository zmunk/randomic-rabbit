# Generated by Django 2.2.5 on 2020-05-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
                ('next_update_time', models.IntegerField(default=1)),
            ],
        ),
    ]
