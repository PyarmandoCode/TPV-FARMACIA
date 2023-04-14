from django.db import models


class Categorias(models.Model):
    nom_cat = models.CharField(max_length=120)
    des_cat=models.TextField(blank=True,null=True)
    color_cat = models.CharField(max_length=60,blank=True,null=True)
    img_cat = models.CharField(max_length=90,blank=True,null=True)
    est_cat = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_cat

    class Meta:
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'Categorias'

class Tipo_Proveedor(models.Model):
    tip_prov = models.CharField(max_length=120)
    des_tip_prov=models.TextField(blank=True,null=True)
    est_tip_prov = models.BooleanField(default=True)

    def __str__(self):
        return self.tip_prov
    
    class Meta:
        verbose_name = 'Tipo_Proveedor'
        verbose_name_plural = 'Tipo_Proveedor'
        ordering = ['id']
        db_table = 'Tipo_Proveedor'


class Proveedores(models.Model):
    nom_prov = models.CharField(max_length=120)
    des_prov=models.TextField(blank=True,null=True)
    dir_prov = models.CharField(max_length=200)
    doc_prov=models.CharField(max_length=12)
    tel_prov=models.CharField(max_length=15)
    email_prov=models.CharField(max_length=25)
    contacto_prov=models.CharField(max_length=120,blank=True,null=True)
    tipo_prov=models.ForeignKey(Tipo_Proveedor,on_delete=models.CASCADE)
    est_prov = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_prov
    
    class Meta:
        verbose_name = 'Proveedores'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']
        db_table = 'Proveedores'


class Marca(models.Model):
    nom_marca = models.CharField(max_length=120)
    des_marca=models.TextField(blank=True,null=True)
    img_marca = models.CharField(max_length=90,blank=True,null=True)
    est_marca = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_marca    
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'
        ordering = ['id']
        db_table = 'Marca'


class Presentacion(models.Model): 
    nom_pre = models.CharField(max_length=120)
    des_pre=models.TextField(blank=True,null=True)
    est_pre = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_pre     

    class Meta:
        verbose_name = 'Presentacion'
        verbose_name_plural = 'Presentacion'
        ordering = ['id']
        db_table = 'Presentacion'         
    
class Productos(models.Model):
     nom_prod = models.CharField(max_length=120)
     cod_barra_prod = models.CharField(max_length=120)
     nom_etiqueta_prod=models.CharField(max_length=12,blank=True,null=True)
     des_prod=models.TextField(blank=True,null=True)
     umedida_prod=models.CharField(max_length=120)
     ubicacion =models.CharField(max_length=120)
     color_prod = models.CharField(max_length=60,blank=True,null=True)
     img_prod = models.CharField(max_length=90,blank=True,null=True)
     cat_prod=models.ForeignKey(Categorias,on_delete=models.CASCADE)
     prov_prod=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
     marca_prod=models.ForeignKey(Marca,on_delete=models.CASCADE)
     present_prod=models.ForeignKey(Presentacion,on_delete=models.CASCADE)
    
     
     #Estos campos deberian ir en compras
     costo_prod=models.DecimalField(max_digits=6,decimal_places=2)
     pre_prod_publico=models.DecimalField(max_digits=6,decimal_places=2)
     
     #Estos campos deberian ir en compras
     acepta_desc_prod=models.BooleanField(default=True)
     acepta_desc_imp=models.BooleanField(default=True)

     def __str__(self):
        return self.nom_prod  
     
     class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        db_table = 'Productos'
     





