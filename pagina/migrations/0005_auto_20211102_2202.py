# Generated by Django 3.2.9 on 2021-11-03 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_auto_20211102_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'Redes Sociais'},
        ),
        migrations.AddField(
            model_name='social',
            name='nome',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='social',
            name='twitter',
            field=models.BooleanField(default=False),
        ),
    ]