# Generated by Django 3.2.5 on 2021-10-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
