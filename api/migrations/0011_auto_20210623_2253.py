# Generated by Django 3.1.7 on 2021-06-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210623_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='userpr/5e63fa39-3bc2-49ee-b9f4-17e02fe75a34/uploads'),
        ),
    ]