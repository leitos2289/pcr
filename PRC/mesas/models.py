from django.db import models

class Persona(models.Model):
    idpersona = models.AutoField(db_column='IDPERSONA', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=100)