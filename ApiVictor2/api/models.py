from django.db import models

# Create your models here.

class TipoHabitacion(models.Model):
    Id_TipoHabitacion = models.AutoField(primary_key=True)
    Habitacion = models.CharField(max_length=100,db_column='Habitacion')
    class Meta:
        db_table="Tipo_Habitacion"

class ServcioHotel(models.Model):
    Id_Servicio = models.AutoField(primary_key=True)
    Servicios = models.CharField(max_length=100,db_column='Servicios')

    class Meta:
        db_table="Servicio_Hotel"
        
class Colores(models.Model):
    Id_Color = models.AutoField(primary_key=True)
    Colores = models.CharField(max_length=100,db_column='Colores')
   
    class Meta:
        db_table="Colores_Diseño"
        
class Funcionalidades(models.Model):
    Id_Funcionalidades = models.AutoField(primary_key=True)
    Funcionalidades = models.CharField(max_length=100,db_column='Funcionalidades')
    class Meta:
        db_table="Funcionalidades"
        
class Facilidad_Uso(models.Model):
    Id_Facilidad = models.AutoField(primary_key=True)
    Facilidad_Uso = models.CharField(max_length=100,db_column='Facilidades de Uso')
    
    class Meta:
        db_table="Facilidad_Uso"
        
class Dispositivos(models.Model):
    Id_Dispositivos = models.AutoField(primary_key=True)
    Dispositivos = models.CharField(max_length=100,db_column='Dispositivos')
    class Meta:
        db_table="Dispositivos"
        
class Idioma(models.Model):
    Id_idioma = models.AutoField(primary_key=True)
    Idioma = models.CharField(max_length=100,db_column='Idiomas')

    class Meta:
        db_table="Idioma"
        
class Redes(models.Model):
    Id_Redes = models.AutoField(primary_key=True)
    Redes_Sociales = models.CharField(max_length=100,db_column='Redes')

    class Meta:
        db_table="Redes"
        
class Contacto(models.Model):
    Id_Contacto = models.AutoField(primary_key=True)
    Contacto = models.CharField(max_length=100,db_column='Contacto')
    
    class Meta:
        db_table="Contacto"
        
class Datos_Reserva(models.Model):
    Id_DatosReserva = models.AutoField(primary_key=True)
    Datos_Reserva = models.CharField(max_length=100,db_column='Datos')

    class Meta:
        db_table="Datos_Reserva"
        
class Proceso_Reserva(models.Model):
    Id_ProcesoReserva = models.AutoField(primary_key=True)
    Proceso_Reserva = models.CharField(max_length=100,db_column='Proceso Reserva')
    
    class Meta:
        db_table="Proceso_Reserva"
        
class Pago(models.Model):
    Id_Pago = models.AutoField(primary_key=True)
    Pagos = models.CharField(max_length=100,db_column='Pagos')
    
    class Meta:
        db_table="Pago"
        
class Calendario(models.Model):
    Id_Calendario = models.AutoField(primary_key=True)
    Calendario = models.CharField(max_length=100,db_column='Calendario')
    class Meta:
        db_table="Calendario"


# class InformacionHotel(models.Model):
#     OPCIONES = (
#         ('a', 'Información sobre habitaciones y tarifas'),
#         ('b', 'Fotos y galería del hotel'),
#         ('c', 'Servicios y comodidades del hotel'),
#         ('d', ' Información sobre atracciones locales y actividades cercanas')
#     )

#     opcion = models.CharField(max_length=1, choices=OPCIONES)
#     contenido = models.TextField()  # Este campo almacenará el contenido relacionado con la opción

#     def __str__(self):
#         return f"{self.get_opcion_display()}: {self.contenido}"
        