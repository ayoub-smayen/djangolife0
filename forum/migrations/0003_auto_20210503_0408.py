# Generated by Django 3.1.7 on 2021-05-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20210503_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AlterField(
            model_name='comments',
            name='file_comment',
            field=models.FileField(upload_to='comments/2021-05-03/docs/O'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postfile',
            field=models.ImageField(upload_to='posts/2021-05-03/doct/O/v/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postimg',
            field=models.ImageField(upload_to='posts/O/p'),
        ),
    ]
