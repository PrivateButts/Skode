# Generated by Django 2.1 on 2018-08-04 07:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel')),
                ('alt', models.CharField(blank=True, max_length=200, null=True)),
                ('caption', ckeditor.fields.RichTextField()),
            ],
        ),
    ]