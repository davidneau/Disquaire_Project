# Generated by Django 3.1.2 on 2021-10-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211026_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.URLField(max_length=10000),
        ),
    ]