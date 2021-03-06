# Generated by Django 3.0.3 on 2020-08-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0009_auto_20200828_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='artcompositing',
            name='poster',
            field=models.ImageField(null=True, upload_to='video/posters/'),
        ),
        migrations.AddField(
            model_name='artmapping',
            name='poster',
            field=models.ImageField(null=True, upload_to='video/posters/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to='video/posters/'),
        ),
        migrations.AlterField(
            model_name='artcompositing',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='artmapping',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
