# Generated by Django 3.0.5 on 2021-01-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvmatchup', '0004_auto_20210122_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='media/'),
        ),
    ]