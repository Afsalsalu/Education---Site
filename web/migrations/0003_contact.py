# Generated by Django 5.0.1 on 2024-02-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
            ],
        ),
    ]