# Generated by Django 3.1.7 on 2021-06-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciepe', '0007_auto_20210616_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='reciepe/W/'),
        ),
    ]
