# Generated by Django 4.1.3 on 2022-11-17 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_servicesmodel_image1_servicesmodel_image10_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesmodel',
            name='image10',
        ),
    ]