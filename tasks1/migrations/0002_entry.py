# Generated by Django 5.0.2 on 2024-02-07 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=10)),
                ('task_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks1.task')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
