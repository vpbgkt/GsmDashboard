# Generated by Django 4.1.7 on 2023-04-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eclass', '0003_remove_eclass_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eclass',
            name='description',
            field=models.TextField(),
        ),
    ]
