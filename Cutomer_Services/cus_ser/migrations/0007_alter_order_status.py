# Generated by Django 4.1 on 2022-09-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cus_ser', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('Out for delivery', 'Out for delivery'), ('delivered', 'delivered')], max_length=200, null=True),
        ),
    ]
