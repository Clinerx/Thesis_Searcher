# Generated by Django 5.0.3 on 2024-03-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_remove_thesis_abstract_remove_thesis_research_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='abstract',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='thesis',
            name='research_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
