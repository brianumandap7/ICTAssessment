# Generated by Django 3.2.16 on 2023-04-19 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_auto_20230419_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='keyboard_office',
            new_name='kb_acer_installed',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='mouse_office',
            new_name='kb_acer_personal',
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_hp_installed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_hp_personal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_lenovo_installed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_lenovo_personal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_others_installed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_others_personal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_samsung_installed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='kb_samsung_personal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
