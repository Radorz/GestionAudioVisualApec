from django.db import models


# Tipos de Equipos
class TipoEquipo(models.Model):
    descripcion = models.CharField(max_length=100)
    estado      = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

# Marcas
class Marca(models.Model):
    descripcion  = models.CharField(max_length=100)
    estado       = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

# Modelos
class Modelo(models.Model):
    marca       = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    estado      = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion} ({self.marca})"

# Tecnologías de Conexión
class TecnologiaConexion(models.Model):
    descripcion = models.CharField(max_length=100)
    estado      = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

# Equipos
class Equipo(models.Model):
    descripcion     = models.CharField(max_length=100)
    numero_serial   = models.CharField(max_length=50)
    service_tag     = models.CharField(max_length=50)
    tipo_equipo     = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    marca           = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo          = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tecnologia_conexion = models.ForeignKey(TecnologiaConexion, on_delete=models.CASCADE)
    estado              = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

# Usuarios
class Usuario(models.Model):
    nombre          = models.CharField(max_length=100)
    cedula          = models.CharField(max_length=11)
    numero_carnet   = models.CharField(max_length=20)
    tipo_usuario    = models.CharField(max_length=50, choices=[('Profesor', 'Profesor'), ('Estudiante', 'Estudiante'), ('Empleado', 'Empleado')])
    tipo_persona    = models.CharField(max_length=20, choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')])
    estado          = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Empleados
class Empleado(models.Model):
    nombre          = models.CharField(max_length=100)
    cedula          = models.CharField(max_length=11)
    tanda_labor     = models.CharField(max_length=50, choices=[('Matutina', 'Matutina'), ('Vespertina', 'Vespertina'), ('Nocturna', 'Nocturna')])
    fecha_ingreso   = models.DateField(null=True, blank=True)
    estado          = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Préstamos y Devoluciones
class Prestamo(models.Model):
    empleado            = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    equipo              = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario             = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo      = models.DateTimeField(null=True, blank=True)
    fecha_devolucion    = models.DateTimeField(null=True, blank=True)
    comentario          = models.TextField(null=True, blank=True)
    estado              = models.BooleanField(default=True)


    def __str__(self):
        return f"Préstamo de {self.equipo} a {self.usuario}"