# Generated by Django 3.1.7 on 2021-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciepe', '0009_auto_20210621_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='reciepe/Z/'),
        ),
    ]