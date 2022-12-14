# Generated by Django 3.2.15 on 2022-09-14 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_medico_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='convenio',
            options={'verbose_name': 'Convênio', 'verbose_name_plural': 'Convênios'},
        ),
        migrations.AddField(
            model_name='medico',
            name='convenios',
            field=models.ManyToManyField(related_name='medico', through='core.Atende', to='core.Convenio'),
        ),
    ]
