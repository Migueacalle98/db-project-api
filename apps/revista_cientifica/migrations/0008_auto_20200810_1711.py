# Generated by Django 3.1 on 2020-08-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista_cientifica', '0007_auto_20200810_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='media/files'),
        ),
    ]