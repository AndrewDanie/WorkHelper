# Generated by Django 4.0.6 on 2022-07-18 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helperserver', '0003_rename_order_name_complited_work_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spare_parts',
            old_name='part',
            new_name='order',
        ),
    ]
