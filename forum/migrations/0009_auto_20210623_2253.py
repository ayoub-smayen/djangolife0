# Generated by Django 3.1.7 on 2021-06-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20210623_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='file_comment',
            field=models.FileField(upload_to='comments/2021-06-23/docs/E'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postfile',
            field=models.ImageField(upload_to='posts/2021-06-23/doct/E/v/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postimg',
            field=models.ImageField(upload_to='posts/E/p'),
        ),
    ]
