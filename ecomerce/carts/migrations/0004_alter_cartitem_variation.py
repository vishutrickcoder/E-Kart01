# Generated by Django 4.0.4 on 2022-06-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('carts', '0003_alter_cartitem_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, null=True, to='store.variation'),
        ),
    ]
