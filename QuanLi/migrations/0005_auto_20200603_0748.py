# Generated by Django 3.0.6 on 2020-06-03 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLi', '0004_donvi_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donvi',
            old_name='status',
            new_name='TrangThai',
        ),
    ]