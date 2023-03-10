# Generated by Django 4.0.1 on 2022-12-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_category_tag_projectmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesmodel',
            name='icon',
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='is_home',
            field=models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi? (Sadece 4 Proje Gösterebilirsiniz)'),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='tag',
            field=models.ManyToManyField(to='pages.Tag', verbose_name='Etiket Seçin'),
        ),
    ]
