# Generated by Django 3.1.4 on 2020-12-07 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['id'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
