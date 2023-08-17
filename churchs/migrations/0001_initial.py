# Generated by Django 4.2.2 on 2023-07-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Churchs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church_name', models.CharField(max_length=200, null=True)),
                ('church_branch', models.CharField(max_length=200, null=True)),
                ('church_tree', models.CharField(max_length=200, null=True)),
                ('church_synod', models.CharField(choices=[('SPA - Antsiranana', 'SPA - Antsiranana'), (' SPAVA - Sambava', ' SPAVA - Sambava'), ('SPSofia - Antsohihy', 'SPSofia - Antsohihy'), ('SPBM - Mahajanga', 'SPBM - Mahajanga'), ('SPAI - Ambatondrazaka', 'SPAI - Ambatondrazaka'), ('SPTM - Toamasina', 'SPTM - Toamasina'), ('SPAnta - Antananarivo', 'SPAnta - Antananarivo'), ('SPN - Marolambo', 'SPN - Marolambo'), ('SPAN - Mananjary', 'SPAN - Mananjary'), ('SPMa - Manakara', 'SPMa - Manakara'), ('SPAts - Farafangana', 'SPAts - Farafangana'), ('SPAV - Vondrozo', 'SPAV - Vondrozo'), ('SPFa - Faradofay', 'SPFa - Faradofay'), ('SPAA - Ambovombe Androy', 'SPAA - Ambovombe Androy'), ('SPAB - Betroka', 'SPAB - Betroka'), ('SPH - Ihosy', 'SPH - Ihosy'), ('SPBA - Betioky Atsimo', 'SPBA - Betioky Atsimo'), ('SPFT - Toliara', 'SPFT - Toliara'), ('SPAf - Fianarantsoa', 'SPAf - Fianarantsoa'), ('SPATsim - Ambatofinandrahana', 'SPATsim - Ambatofinandrahana'), ('SPM - Morondava', 'SPM - Morondava'), ('SPAFI - Fandriana', 'SPAFI - Fandriana'), ('SPAM - Antsirabe', 'SPAM - Antsirabe'), ('SPMel - Maintirano', 'SPMel - Maintirano'), ('FLME - Europa', 'FLME - Europa')], max_length=200, null=True)),
                ('type_of', models.CharField(choices=[('Eglise', 'Eglise'), ('Hôpital', 'Hôpital'), ('Centre', 'Centre'), ('Ecole', 'Ecole')], max_length=200, null=True)),
                ('located_at', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('neighborhood', models.CharField(max_length=200, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
