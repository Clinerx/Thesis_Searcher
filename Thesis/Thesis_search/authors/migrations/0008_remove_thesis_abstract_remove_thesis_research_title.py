# Generated by Django 5.0.3 on 2024-03-09 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0007_thesis_abstract_thesis_research_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='research_title',
        ),
    ]
