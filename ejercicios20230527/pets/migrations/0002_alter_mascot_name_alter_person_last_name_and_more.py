# Generated by Django 4.2.1 on 2023-05-31 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascot',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
