# Generated by Django 3.1.4 on 2022-11-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invent',
            name='selling_price',
            field=models.CharField(default=True, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invent',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
