# Generated by Django 3.1.7 on 2021-06-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210616_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to='musicas/14/V'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='musicatsong/14/V'),
        ),
    ]
