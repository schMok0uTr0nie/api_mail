# Generated by Django 4.1.4 on 2023-01-09 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail_api', '0004_alter_client_operator_alter_client_tag_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='status',
        ),
        migrations.AddField(
            model_name='mail',
            name='time_gap_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Окончание периода'),
        ),
        migrations.AddField(
            model_name='mail',
            name='time_gap_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Начало периода'),
        ),
        migrations.AddField(
            model_name='message',
            name='sent_status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mail_api.client', verbose_name='Клиенты'),
        ),
    ]
