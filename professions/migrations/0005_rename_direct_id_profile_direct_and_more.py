# Generated by Django 4.0.3 on 2022-05-25 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0004_alter_direction_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='direct_id',
            new_name='direct',
        ),
        migrations.RenameField(
            model_name='userdirect',
            old_name='direct_id',
            new_name='direct',
        ),
        migrations.RenameField(
            model_name='userdirect',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userprof',
            old_name='profile_id',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='userprof',
            old_name='user_id',
            new_name='user',
        ),
    ]
