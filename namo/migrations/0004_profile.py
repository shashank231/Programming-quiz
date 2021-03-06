# Generated by Django 3.0.6 on 2020-06-16 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('namo', '0003_subject_card_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='images/profile/default.png', null=True, upload_to='images/profile')),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('subjects', models.ManyToManyField(blank=True, null=True, to='namo.Subject')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
