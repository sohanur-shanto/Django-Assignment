# Generated by Django 3.2.8 on 2021-12-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
    ]
