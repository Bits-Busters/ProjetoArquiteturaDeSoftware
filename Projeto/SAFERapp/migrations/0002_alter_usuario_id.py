# Generated by Django 5.1.4 on 2024-12-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAFERapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]