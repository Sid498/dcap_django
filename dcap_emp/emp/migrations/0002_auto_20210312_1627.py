# Generated by Django 3.0.5 on 2021-03-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
