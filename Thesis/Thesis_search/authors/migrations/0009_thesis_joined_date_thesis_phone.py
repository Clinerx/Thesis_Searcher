# Generated by Django 5.0.3 on 2024-03-09 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0008_remove_thesis_abstract_remove_thesis_research_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='thesis',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
