# Generated by Django 4.0.3 on 2022-06-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shamim', '0006_remove_order_tag_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(related_name='product_set', to='shamim.tag'),
        ),
    ]
