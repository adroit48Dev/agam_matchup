# Generated by Django 3.0.5 on 2021-01-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvmatchup', '0003_auto_20210122_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='templ_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]