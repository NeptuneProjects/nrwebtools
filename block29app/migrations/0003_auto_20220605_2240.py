# Generated by Django 3.2.5 on 2022-06-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block29app', '0002_auto_20220605_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='block29',
            name='formatted',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='block29',
            name='coll_desc',
            field=models.TextField(blank=True, default=None),
        ),
    ]