# Generated by Django 3.0.6 on 2020-06-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0017_auto_20200618_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]