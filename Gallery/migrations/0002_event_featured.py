# Generated by Django 2.1 on 2018-08-04 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_set', to='Gallery.Picture'),
        ),
    ]
