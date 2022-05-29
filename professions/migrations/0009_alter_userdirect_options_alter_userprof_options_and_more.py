# Generated by Django 4.0.3 on 2022-05-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0008_alter_userdirect_options_alter_userprof_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdirect',
            options={'ordering': ['directionIndex']},
        ),
        migrations.AlterModelOptions(
            name='userprof',
            options={'ordering': ['profileIndex']},
        ),
        migrations.RenameField(
            model_name='userdirect',
            old_name='position',
            new_name='directionIndex',
        ),
        migrations.RenameField(
            model_name='userprof',
            old_name='profile',
            new_name='profileIndex',
        ),
    ]
