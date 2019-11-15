# Generated by Django 2.2.7 on 2019-11-15 02:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autores',
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='autores.Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editoriales.Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.datetime(2019, 11, 15, 2, 15, 33, 241012, tzinfo=utc)),
        ),
    ]
