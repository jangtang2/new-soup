# Generated by Django 2.2.5 on 2020-11-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20201103_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]