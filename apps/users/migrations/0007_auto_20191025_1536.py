# Generated by Django 2.0 on 2019-10-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191025_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='用户头像'),
        ),
    ]