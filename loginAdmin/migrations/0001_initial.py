# Generated by Django 3.1.2 on 2020-11-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=25)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
