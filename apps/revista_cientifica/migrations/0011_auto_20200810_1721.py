# Generated by Django 3.1 on 2020-08-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista_cientifica', '0010_auto_20200810_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='ORCID',
            field=models.BigIntegerField(default=1000000000000000, max_length=16, null=True, unique=True),
        ),
    ]
