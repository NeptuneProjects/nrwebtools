# Generated by Django 3.2.5 on 2022-06-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block29app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block29',
            name='atadt1',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='atadt2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='coll_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='block29',
            name='coll_len',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='coll_long',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='cross',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='block29',
            name='mob',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='pfa',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='umuic',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='watch',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='block29',
            name='watch_len',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
