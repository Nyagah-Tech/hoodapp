# Generated by Django 2.2.8 on 2020-01-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0007_neighbourhood_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/'),
        ),
    ]