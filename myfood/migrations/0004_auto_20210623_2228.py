# Generated by Django 3.1.7 on 2021-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfood', '0003_auto_20210621_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpost',
            name='image',
            field=models.FileField(blank=True, upload_to='food/67/2021'),
        ),
        migrations.AlterField(
            model_name='foodpostimage',
            name='images',
            field=models.FileField(upload_to='foodposts/2021/images/63'),
        ),
    ]
