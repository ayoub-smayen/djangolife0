# Generated by Django 3.1.7 on 2021-04-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=8)),
                ('message', models.TextField()),
            ],
        ),
    ]
