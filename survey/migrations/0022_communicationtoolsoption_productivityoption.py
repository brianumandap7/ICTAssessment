# Generated by Django 3.2.16 on 2023-04-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0021_auto_20230426_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunicationToolsOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductivityOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]