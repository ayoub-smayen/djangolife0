# Generated by Django 3.1.7 on 2021-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210621_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='userpr/be9f4aa9-a7aa-47c9-bb63-01f71ece9d80/uploads'),
        ),
    ]