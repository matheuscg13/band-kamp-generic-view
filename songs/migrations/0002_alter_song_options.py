# Generated by Django 4.0.7 on 2023-02-23 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('id',)},
        ),
    ]
