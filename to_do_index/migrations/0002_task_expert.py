# Generated by Django 3.2 on 2021-04-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expert',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]