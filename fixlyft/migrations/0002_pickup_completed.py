# Generated by Django 3.1.1 on 2020-09-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixlyft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]