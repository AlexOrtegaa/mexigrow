# Generated by Django 4.2.2 on 2023-07-06 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_proyectinstance_date_acquired_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectinstance',
            name='prubea',
            field=models.DateField(blank=True, help_text='Fecha de unión al proyecto', null=True),
        ),
    ]
