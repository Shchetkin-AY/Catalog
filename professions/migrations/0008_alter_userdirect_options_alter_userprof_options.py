# Generated by Django 4.0.3 on 2022-05-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0007_alter_userdirect_position_alter_userprof_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdirect',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='userprof',
            options={'ordering': ['position']},
        ),
    ]
