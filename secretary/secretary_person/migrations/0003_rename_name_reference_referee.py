# Generated by Django 5.0.6 on 2024-05-23 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretary_person', '0002_hobby_reference_skill_workhistory_responsibility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='name',
            new_name='referee',
        ),
    ]
