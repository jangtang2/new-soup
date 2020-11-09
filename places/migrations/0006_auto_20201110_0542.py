# Generated by Django 2.2.5 on 2020-11-09 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20201103_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='etc',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='etc',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.Place'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(choices=[('서울특별시', '서울특별시'), ('부산광역시', '부산광역시'), ('대구광역시', '대구광역시'), ('인천광역시', '인천광역시'), ('광주광역시', '광주광역시'), ('대전광역시', '대전광역시'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('제주특별자치도', '제주특별자치도')], max_length=80),
        ),
        migrations.AlterField(
            model_name='place',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
