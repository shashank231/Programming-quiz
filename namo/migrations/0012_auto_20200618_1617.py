# Generated by Django 3.0.6 on 2020-06-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0011_auto_20200618_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='anna',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='comt',
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to=''),
        ),
    ]
