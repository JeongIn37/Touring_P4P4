# Generated by Django 3.0 on 2020-09-04 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='일정'),
        ),
    ]
