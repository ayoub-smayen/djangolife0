# Generated by Django 3.1.7 on 2021-06-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipevideo', '0008_auto_20210623_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipevideo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='reciepevideos/H/'),
        ),
        migrations.AlterField(
            model_name='recipevideo',
            name='url',
            field=models.FileField(blank=True, null=True, upload_to='rvideos/H/videorecipes'),
        ),
        migrations.AlterField(
            model_name='recipevideo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='recipesvideosusers/H/'),
        ),
    ]
