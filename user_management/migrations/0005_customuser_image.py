# Generated by Django 2.2.15 on 2020-08-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]