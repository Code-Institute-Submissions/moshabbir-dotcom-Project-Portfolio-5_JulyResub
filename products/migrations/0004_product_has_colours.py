# Generated by Django 3.2 on 2022-04-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_category_product_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_colours',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]