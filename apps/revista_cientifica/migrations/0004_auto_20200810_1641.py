# Generated by Django 3.1 on 2020-08-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista_cientifica', '0003_auto_20200807_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='\\media'),
        ),
    ]