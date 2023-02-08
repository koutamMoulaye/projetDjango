# Generated by Django 4.1.2 on 2022-10-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('realisateur', models.CharField(max_length=100)),
                ('annee_de_sortie', models.IntegerField()),
                ('nombre_episode', models.IntegerField()),
            ],
        ),
    ]
