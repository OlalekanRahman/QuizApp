# Generated by Django 3.2 on 2021-04-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active mode'),
        ),
    ]
