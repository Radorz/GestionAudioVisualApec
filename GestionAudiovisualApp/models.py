from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

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
# class Usuario(models.Model):
#     nombre          = models.CharField(max_length=100)
#     cedula          = models.CharField(max_length=11)
#     numero_carnet   = models.CharField(max_length=20)
#     tipo_usuario    = models.CharField(max_length=50, choices=[('Profesor', 'Profesor'), ('Estudiante', 'Estudiante'), ('Empleado', 'Empleado')])
#     tipo_persona    = models.CharField(max_length=20, choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')])
#     estado          = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nombre

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, cedula, password=None, **extra_fields):
        if not cedula:
            raise ValueError('El usuario debe tener una cédula')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        user = self.model(nombre=nombre, cedula=cedula, **extra_fields)
        user.set_password(cedula)  # Establecer la cédula como contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, cedula, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(nombre, cedula, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100, unique=True)
    cedula = models.CharField(max_length=11, unique=True)
    numero_carnet = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=50, choices=[('Profesor', 'Profesor'), ('Estudiante', 'Estudiante'), ('Empleado', 'Empleado')])
    tipo_persona = models.CharField(max_length=20, choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')])
    estado = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre'
    REQUIRED_FIELDS = ['cedula']

    def __str__(self):
        return self.nombre

    def is_empleado(self):
        return self.tipo_usuario == 'Empleado'


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