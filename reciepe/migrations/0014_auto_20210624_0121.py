# Generated by Django 3.1.7 on 2021-06-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciepe', '0013_auto_20210624_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='reciepe/L/'),
        ),
    ]
