# Generated by Django 3.2.18 on 2023-06-12 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20230612_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='prov_prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.proveedores'),
        ),
    ]
