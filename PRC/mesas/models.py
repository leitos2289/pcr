from django.db import models

class Persona(models.Model):
    idpersona = models.AutoField(db_column='IDPERSONA', primary_key=True)
    cedula = models.CharField(db_column='CEDULA', max_length=10,null=False)
    nombre = models.CharField(db_column='NOMBRE', max_length=100,null=False)
    direccion = models.CharField(db_column='DIRECCION', max_length=100,null=False,blank=True)
    tefefono = models.CharField(db_column='TELEFONO', max_length=100,null=False,blank=True)

    class Meta:
        managed = True
        db_table = 'PERSONA'

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    idmesa = models.AutoField(db_column='IDMESA', primary_key=True)
    personaacobrar = models.ForeignKey(Persona, models.DO_NOTHING, db_column='PERSONAACOBRAR',null=False)
    numerointegrantes = models.IntegerField(default=0,db_column='NUMEROINTEGRANTES',null=False)
    valoracobra = models.DecimalField(db_column='VALORACOBRA',max_digits=50, decimal_places=20,null=False)
    fechacobro= models.DateField(db_column='FECHACOBRO',null=True,blank=True)
    muere = models.IntegerField(default=0, db_column='MUERE', null=False)

    class Meta:
        managed = True
        db_table = 'MESA'

    def __str__(self):
        return  str(self.idmesa) + str(self.personaacobrar)

class Integrante(models.Model):
    idintegrante = models.AutoField(db_column='IDINTEGRANTE', primary_key=True)
    mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='MESAPERTENECE', null=False)
    persona=models.ForeignKey(Persona, models.DO_NOTHING, db_column='PERSONAINTEGRANTE',null=False)
    color=models.CharField(db_column='COLOR', max_length=100,null=False)
    numeromensaje=models.CharField(db_column='NUMEROMENSAJE', max_length=100,null=False)
    muere = models.IntegerField(default=0, db_column='MUERE', null=False)

    class Meta:
        managed = True
        db_table = 'INTEGRANTE'

class Retejida(models.Model):
    idretejida = models.AutoField(db_column='IDRETEJIDA', primary_key=True)
    mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='MESACOBRO', null=False)
    valoracobro = models.DecimalField(db_column='VALORACOBRO', max_digits=50, decimal_places=20, null=False)
    fechapago = models.DateField(db_column='FECHAPAGO', null=False)
    fechacobro = models.DateField(db_column='FECHACOBRO', null=True,blank=True)

    class Meta:
        managed = True
        db_table = 'RETEJIDA'