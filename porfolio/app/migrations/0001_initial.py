# Generated by Django 4.1.4 on 2022-12-09 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField()),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=100)),
                ('urls', models.URLField()),
            ],
        ),
    ]