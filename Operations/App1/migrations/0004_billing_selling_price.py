# Generated by Django 3.1.4 on 2022-11-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_billing'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='selling_price',
            field=models.CharField(default=True, max_length=1000),
            preserve_default=False,
        ),
    ]