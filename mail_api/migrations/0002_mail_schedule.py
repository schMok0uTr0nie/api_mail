# Generated by Django 4.1.4 on 2023-01-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='schedule',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Расписание'),
        ),
    ]
