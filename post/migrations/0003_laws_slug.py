# Generated by Django 4.2.1 on 2023-06-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_category_servicecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='laws',
            name='slug',
            field=models.SlugField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
