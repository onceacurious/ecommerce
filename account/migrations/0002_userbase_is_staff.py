# Generated by Django 3.2.8 on 2021-10-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]