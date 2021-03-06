# Generated by Django 2.1 on 2018-09-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
