# Generated by Django 3.2.17 on 2023-02-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='followerId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='friends',
            name='userId',
            field=models.IntegerField(),
        ),
    ]