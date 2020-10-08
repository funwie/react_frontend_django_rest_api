# Generated by Django 3.1.2 on 2020-10-06 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_search', '0002_auto_20201006_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_item', to='order_search.item'),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='order_search.order'),
        ),
    ]
