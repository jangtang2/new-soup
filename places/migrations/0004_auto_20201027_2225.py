# Generated by Django 2.2.5 on 2020-10-27 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20201027_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='etc',
            options={'verbose_name': 'ETC'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterField(
            model_name='place',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='places.Amenity'),
        ),
        migrations.AlterField(
            model_name='place',
            name='etcs',
            field=models.ManyToManyField(blank=True, to='places.ETC'),
        ),
        migrations.AlterField(
            model_name='place',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='places.Facility'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('file', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]