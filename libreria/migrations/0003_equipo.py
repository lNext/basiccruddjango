# Generated by Django 5.0 on 2023-12-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libreria", "0002_rename_decription_libro_descripcion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "imagen",
                    models.ImageField(
                        null=True, upload_to="imagenes/", verbose_name="Imagen"
                    ),
                ),
                ("cargo", models.TextField(null=True, verbose_name="Cargo")),
            ],
        ),
    ]