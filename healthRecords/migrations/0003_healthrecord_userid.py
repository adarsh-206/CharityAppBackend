# Generated by Django 5.0.1 on 2024-02-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthRecords', '0002_alter_healthrecord_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthrecord',
            name='userId',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
