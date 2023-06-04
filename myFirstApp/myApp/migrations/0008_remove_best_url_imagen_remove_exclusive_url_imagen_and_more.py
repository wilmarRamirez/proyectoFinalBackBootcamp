# Generated by Django 4.2.1 on 2023-06-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_remove_exclusive_created_remove_exclusive_is_removed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='best',
            name='url_imagen',
        ),
        migrations.RemoveField(
            model_name='exclusive',
            name='url_imagen',
        ),
        migrations.RemoveField(
            model_name='latestblog',
            name='url_imagen',
        ),
        migrations.AddField(
            model_name='best',
            name='imagen',
            field=models.ImageField(null=True, upload_to='best'),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='imagen',
            field=models.ImageField(null=True, upload_to='exclusive'),
        ),
        migrations.AddField(
            model_name='latestblog',
            name='imagen',
            field=models.ImageField(null=True, upload_to='latestBlog'),
        ),
    ]