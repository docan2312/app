# Generated by Django 3.0.6 on 2020-06-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLi', '0008_auto_20200605_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donvi',
            name='status',
            field=models.BooleanField(null=True, verbose_name={'False': 'Tạm ngưng hoạt động', 'True': 'Đang hoạt động'}),
        ),
    ]
