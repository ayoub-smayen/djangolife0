# Generated by Django 3.1.7 on 2021-06-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210616_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='userpr/d053a4f6-0177-411f-8eef-11c47516165e/uploads'),
        ),
    ]
