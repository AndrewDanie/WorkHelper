# Generated by Django 4.0.6 on 2022-07-18 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helperserver', '0002_remove_order_completed_work_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complited_work',
            old_name='order_name',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='spare_parts',
            old_name='part_name',
            new_name='part',
        ),
    ]
