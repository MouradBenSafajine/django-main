# Generated by Django 4.2.1 on 2023-05-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]
