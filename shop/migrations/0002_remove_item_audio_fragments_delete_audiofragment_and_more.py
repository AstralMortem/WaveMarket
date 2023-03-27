# Generated by Django 4.1.7 on 2023-03-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='audio_fragments',
        ),
        migrations.DeleteModel(
            name='AudioFragment',
        ),
        migrations.AddField(
            model_name='item',
            name='audio_fragments',
            field=models.FileField(blank=True, null=True, upload_to='product/audio/%Y/%m/%d'),
        ),
    ]
