# Generated by Django 3.2.3 on 2021-06-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0003_auto_20210603_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
