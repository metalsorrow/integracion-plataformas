# Generated by Django 3.0.6 on 2020-06-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion_backend', '0002_auto_20200606_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='idUser',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
