# Generated by Django 3.1.2 on 2020-10-06 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_search', '0005_auto_20201006_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_item', to='order_search.item'),
        ),
    ]