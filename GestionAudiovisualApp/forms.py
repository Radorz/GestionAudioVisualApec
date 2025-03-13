from django import forms
from .models import Modelo, Marca, Equipo, TipoEquipo, Usuario, Empleado, Prestamo
import re
from django.core.exceptions import ValidationError

class ModeloForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione una marca"
    )
    class Meta:
        model = Modelo
        fields = ['marca', 'descripcion', 'estado']


class EquipoForm(forms.ModelForm):
    tipo_equipo = forms.ModelChoiceField(
        queryset= TipoEquipo.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un Tipo Equipo"
    )
    class Meta:
        model = Equipo
        fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion', 'estado']

def validar_cedula(value):
    if not re.fullmatch(r'\d{11}', value):
        raise ValidationError('La cédula debe tener 11 dígitos numéricos.')

    coeficientes = [1, 2] * 5  # Alterna entre 1 y 2
    digitos = [int(d) for d in value[:10]]
    digito_verificador = int(value[10])

    suma = 0
    for i, digito in enumerate(digitos):
        producto = digito * coeficientes[i]
        if producto >= 10:
            producto = (producto // 10) + (producto % 10)
        suma += producto

    resto = suma % 10
    digito_calculado = 0 if resto == 0 else 10 - resto

    if digito_calculado != digito_verificador:
        raise ValidationError('La cédula ingresada no es válida.')
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'cedula', 'numero_carnet', 'tipo_usuario', 'tipo_persona', 'estado']
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        validar_cedula(cedula)  # Llama a la función de validación
        return cedula
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['cedula'])  # Establecer la cédula como contraseña
        if commit:
            user.save()
        return user

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cedula', 'tanda_labor', 'fecha_ingreso', 'estado']
        widgets = {
        'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        validar_cedula(cedula)  # Llama a la función de validación
        return cedula

class PrestamoForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(
        queryset= Empleado.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Empledo"
    )
    equipo = forms.ModelChoiceField(
        queryset= Equipo.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Equipo"
    )
    usuario = forms.ModelChoiceField( 
        queryset= Usuario.objects.filter(estado=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Usuario"
    )
    class Meta:
        model = Prestamo
        fields = ['empleado', 'equipo', 'usuario', 'fecha_prestamo']
        widgets = {
        'fecha_prestamo': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        'fecha_devolucion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean(self):
        cleaned_data = super().clean()
        equipo = cleaned_data.get('equipo')
        if equipo:
            prestamos_activos = Prestamo.objects.filter(equipo=equipo, fecha_devolucion__isnull=True)
            if prestamos_activos.exists():
                raise ValidationError(f'El equipo {equipo} ya está prestado y no ha sido devuelto.')
        return cleaned_data



class DevolverPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_devolucion', 'comentario']
        widgets = {
        'fecha_devolucion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('fecha_devolucion'):
            raise forms.ValidationError("Debe registrar una fecha de devolución.")
        return cleaned_data


class ConsultaCriteriosForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(estado=True), required=False, label="Usuario")
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.filter(estado=True), required=False, label="Equipo")
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Inicio")
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Fin")
    tipo_equipo = forms.ModelChoiceField(queryset=TipoEquipo.objects.filter(estado=True), required=False, label="Tipo de Equipo")