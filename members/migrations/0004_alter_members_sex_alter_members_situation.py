# Generated by Django 4.2.2 on 2023-06-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_members_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='sex',
            field=models.CharField(blank=True, choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Veuillez indiquer votre sexe', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='situation',
            field=models.CharField(blank=True, choices=[('Marié', 'Marié'), ('Divorcé', 'Divorcé'), ('Célibataire', 'Célibataire')], default='Votre Situation familiale', max_length=200, null=True),
        ),
    ]
