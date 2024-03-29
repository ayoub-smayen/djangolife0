# Generated by Django 3.1.7 on 2021-06-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210616_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to='musicas/31/t'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='musicatsong/31/t'),
        ),
    ]
