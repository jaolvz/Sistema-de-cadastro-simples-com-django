# Generated by Django 5.1.4 on 2024-12-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_capa/'),
        ),
    ]
