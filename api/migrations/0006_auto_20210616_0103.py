# Generated by Django 3.1.7 on 2021-06-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210502_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='userpr/8ba6734e-ae1e-4810-b1e2-93699feb6974/uploads'),
        ),
    ]
