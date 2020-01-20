from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key = True) 
    nombre = models.CharField("Nombre Cliente",max_length =200,blank = False,null = False)
    dui = models.CharField("D.U.I.",max_length = 15,blank = False,null = False)
    direccion = models.TextField("Dirreccion")
    telefono = models.CharField("Telefono",max_length = 15,blank = True,null = True)
    email = models.EmailField("Correo")

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Cargo(models.Model): 
    id = models.AutoField(primary_key = True) 
    cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE,blank = False,null = False)
    fecha = models.DateField("Fecha")
    documento = models.CharField("Documento",max_length = 15,blank = False,null = False)
    val_cargo = models.DecimalField("Cargo",max_digits = 12,decimal_places = 2)
    val_abono = models.DecimalField("Abono",max_digits = 12,decimal_places = 2,default = 0)
    val_saldo = models.DecimalField("Saldo",max_digits = 12,decimal_places = 2)

    class Meta():
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']    
    
    def __str__(self):
        return '# %s - (%s / %s) Saldo: $ %s' % (self.id,self.cliente,self.documento,self.val_saldo)

class Abono(models.Model):
    id = models.AutoField(primary_key = True)
    cargo = models.ForeignKey(Cargo,on_delete = models.CASCADE,blank = False,null = False)
    fecha = models.DateField("Fecha")
    val_abono = models.DecimalField("Abono",max_digits=12,decimal_places=2)

    class Meta():
        verbose_name = 'Abono'
        verbose_name_plural = 'Abonos'
        ordering = ['id']

    def __str__(self):
        return "# %s - (%s / %s)" % (self.id,self.cargo,self.val_abono)
    
