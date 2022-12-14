# Generated by Django 3.2.15 on 2022-09-14 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_medico_idamb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atende',
            options={'verbose_name': 'Médico x convênio', 'verbose_name_plural': 'Médicos x convênios'},
        ),
        migrations.AddField(
            model_name='medico',
            name='convenios',
            field=models.ManyToManyField('Convenio', 'medico', through='Atende'),
        ),
    ]
