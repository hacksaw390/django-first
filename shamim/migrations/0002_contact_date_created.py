# Generated by Django 4.0.3 on 2022-06-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shamim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
