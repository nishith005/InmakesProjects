# Generated by Django 4.1.5 on 2023-01-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hhhg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
