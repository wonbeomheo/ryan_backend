# Generated by Django 5.1 on 2024-09-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('TS', 'Technical Skills'), ('SS', 'Soft Skills')], max_length=2, unique=True),
        ),
    ]
