# Generated by Django 2.2.15 on 2020-09-20 12:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCategory',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0001)])),
                ('description', models.TextField(max_length=500)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_management.MyCategory')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
