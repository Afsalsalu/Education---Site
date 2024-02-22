# Generated by Django 5.0.2 on 2024-02-16 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_media_remove_teachers_facebook_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.AddField(
            model_name='teachers',
            name='facebook',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='instagram',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='twitter',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='whatsapp',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
    ]