# Generated by Django 4.0.3 on 2022-05-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0002_rename_direct_pos_userdirect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
