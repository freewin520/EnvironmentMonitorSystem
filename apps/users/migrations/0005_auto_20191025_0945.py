# Generated by Django 2.0 on 2019-10-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191025_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.IntegerField(choices=[(0, '冻结'), (1, '活跃')], default=1, verbose_name='状态'),
        ),
    ]
