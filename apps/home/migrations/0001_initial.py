# Generated by Django 3.2.18 on 2023-06-06 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cat', models.CharField(max_length=120)),
                ('des_cat', models.TextField(blank=True, null=True)),
                ('img_cat', models.ImageField(blank=True, null=True, upload_to='categorias/')),
                ('est_cat', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categorias',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_color', models.CharField(max_length=120)),
                ('est_color', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Color',
                'db_table': 'Color',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_marca', models.CharField(max_length=120)),
                ('des_marca', models.TextField(blank=True, null=True)),
                ('img_marca', models.CharField(blank=True, max_length=90, null=True)),
                ('est_marca', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marca',
                'db_table': 'Marca',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pre', models.CharField(max_length=120)),
                ('des_pre', models.TextField(blank=True, null=True)),
                ('est_pre', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Presentacion',
                'verbose_name_plural': 'Presentacion',
                'db_table': 'Presentacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_prov', models.CharField(max_length=120)),
                ('des_tip_prov', models.TextField(blank=True, null=True)),
                ('est_tip_prov', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo_Proveedor',
                'verbose_name_plural': 'Tipo_Proveedor',
                'db_table': 'Tipo_Proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prov', models.CharField(max_length=120)),
                ('des_prov', models.TextField(blank=True, null=True)),
                ('dir_prov', models.CharField(max_length=200)),
                ('doc_prov', models.CharField(max_length=12)),
                ('tel_prov', models.CharField(max_length=15)),
                ('email_prov', models.CharField(max_length=25)),
                ('contacto_prov', models.CharField(blank=True, max_length=120, null=True)),
                ('est_prov', models.BooleanField(default=True)),
                ('tipo_prov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipo_proveedor')),
            ],
            options={
                'verbose_name': 'Proveedores',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prod', models.CharField(max_length=120)),
                ('cod_barra_prod', models.CharField(max_length=120)),
                ('nom_etiqueta_prod', models.CharField(blank=True, max_length=12, null=True)),
                ('des_prod', models.TextField(blank=True, null=True)),
                ('umedida_prod', models.CharField(max_length=120)),
                ('ubicacion', models.CharField(max_length=120)),
                ('img_prod', models.CharField(blank=True, max_length=90, null=True)),
                ('costo_prod', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pre_prod_publico', models.DecimalField(decimal_places=2, max_digits=6)),
                ('acepta_desc_prod', models.BooleanField(default=True)),
                ('acepta_desc_imp', models.BooleanField(default=True)),
                ('cat_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categorias')),
                ('color_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.color')),
                ('marca_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.marca')),
                ('present_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.presentacion')),
                ('prov_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.proveedores')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='categorias',
            name='color_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.color'),
        ),
    ]
