# Generated by Django 3.2.9 on 2021-11-03 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_rename_link_social_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='nome',
            new_name='link',
        ),
    ]