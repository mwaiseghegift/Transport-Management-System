# Generated by Django 3.2.5 on 2021-08-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210829_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='Totota', max_length=255),
            preserve_default=False,
        ),
    ]
