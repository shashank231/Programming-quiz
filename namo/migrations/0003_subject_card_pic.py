# Generated by Django 3.0.6 on 2020-06-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0002_subject_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='card_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
