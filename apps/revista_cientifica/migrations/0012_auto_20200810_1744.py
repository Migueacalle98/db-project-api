# Generated by Django 3.1 on 2020-08-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista_cientifica', '0011_auto_20200810_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='ORCID',
            field=models.BigIntegerField(default=1000000000000000, null=True, unique=True),
        ),
    ]