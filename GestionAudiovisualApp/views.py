from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import TipoEquipo, Marca, Modelo, TecnologiaConexion, Equipo, Usuario, Empleado, Prestamo
from django.urls import reverse_lazy, reverse
from django import forms
from django.db.models import Q  # Para manejar consultas complejas
from .forms import ModeloForm, EquipoForm, UsuarioForm, EmpleadoForm, PrestamoForm, DevolverPrestamoForm, ConsultaCriteriosForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")

def inicio(request):
    return render(request, 'inicio.html')


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('inicio')
# CRUD para TipoEquipo
class TipoEquipoListView(ListView):
    model = TipoEquipo
    template_name = 'tipos-equipos/tipoequipo_list.html'
    context_object_name = 'tipos'  # Cambiar el nombre en el contexto
    paginate_by = 10  # Si quieres paginación, puedes agregar esto

    def get_queryset(self):
        queryset = TipoEquipo.objects.all()
        query = self.request.GET.get('q')  # Obtener el término de búsqueda
        if query:
            queryset = queryset.filter(
                Q(descripcion__icontains=query)  # Buscar por descripción
            )
        return queryset

class TipoEquipoCreateView(CreateView):
    model = TipoEquipo
    fields = ['id','descripcion']
    template_name = 'tipos-equipos/tipoequipo_form.html'
    success_url = reverse_lazy('tipoequipo-list')
    widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})         
        }

class TipoEquipoUpdateView(UpdateView):
    model = TipoEquipo
    fields = [ 'descripcion']
    template_name = 'tipos-equipos/tipoequipo_form.html'
    success_url = reverse_lazy('tipoequipo-list')

class TipoEquipoDeleteView(DeleteView):
    model = TipoEquipo
    template_name = 'tipos-equipos/tipoequipo_confirm_delete.html'
    success_url = reverse_lazy('tipoequipo-list')

class ToggleEstadoTipoEquipoView(View):
    def post(self, request, pk):
        tipo_equipo = get_object_or_404(TipoEquipo, pk=pk)
        tipo_equipo.estado = not tipo_equipo.estado  # Cambiar el estado
        tipo_equipo.save()
        return redirect(reverse('tipoequipo-list'))

class MarcaListView(ListView):
    model = Marca
    template_name = 'marcas/marca_list.html'
    context_object_name = 'marcas'
    def get_queryset(self):
        queryset = Marca.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query)
            )
        return queryset

class MarcaCreateView(CreateView):
    model = Marca
    fields = ['descripcion']
    template_name = 'marcas/marca_form.html'
    success_url = reverse_lazy('marca-list')

class MarcaUpdateView(UpdateView):
    model = Marca
    fields = ['descripcion']
    template_name = 'marcas/marca_form.html'
    success_url = reverse_lazy('marca-list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marcas/marca_confirm_delete.html'
    success_url = reverse_lazy('marca-list')

class ToggleEstadoMarcaView(View):
    def post(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        marca.estado = not marca.estado  # Cambiar el estado
        marca.save()
        return redirect(reverse('marca-list'))

# Modelo Views
class ModeloListView(ListView):
    model = Modelo
    template_name = 'modelos/modelo_list.html'
    context_object_name = 'modelos'
    def get_queryset(self):
        queryset = Modelo.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(descripcion__icontains=query) | Q(marca__descripcion__icontains=query)
            )
        return queryset

class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'modelos/modelo_form.html'
    success_url = reverse_lazy('modelo-list')

class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'modelos/modelo_form.html'
    success_url = reverse_lazy('modelo-list')
    
class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = 'modelos/modelo_confirm_delete.html'
    success_url = reverse_lazy('modelo-list')


class ToggleEstadoModeloView(View):
    def post(self, request, pk):
        modelo = get_object_or_404(Modelo, pk=pk)
        modelo.estado = not modelo.estado  # Cambiar el estado
        modelo.save()
        return redirect(reverse('modelo-list'))
# Tecnología de Conexión Views
class TecnologiaConexionListView(ListView):
    model = TecnologiaConexion
    template_name = 'tecnologia-conexion/tecnologiaconexion_list.html'
    context_object_name = 'tecnologias'
    def get_queryset(self):
        queryset = TecnologiaConexion.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(descripcion__icontains=query)
            )
        return queryset

class TecnologiaConexionCreateView(CreateView):
    model = TecnologiaConexion
    fields = ['descripcion']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionUpdateView(UpdateView):
    model = TecnologiaConexion
    fields = ['descripcion']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionDeleteView(DeleteView):
    model = TecnologiaConexion
    template_name = 'tecnologia-conexion/tecnologiaconexion_confirm_delete.html'
    success_url = reverse_lazy('tecnologiaconexion-list')
class ToggleEstadoTecnologiaConexionView(View):
    def post(self, request, pk):
        tecnologia = get_object_or_404(TecnologiaConexion, pk=pk)
        tecnologia.estado = not tecnologia.estado  # Cambiar el estado
        tecnologia.save()
        return redirect(reverse('tecnologiaconexion-list'))
class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipos/equipo_list.html'
    context_object_name = 'equipos'
    def get_queryset(self):
        queryset = Equipo.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(descripcion__icontains=query) | Q(marca__descripcion__icontains=query) | Q(modelo__descripcion__icontains=query)
            )
        return queryset


# Vista para crear un nuevo Equipo
class EquipoCreateView(CreateView):
    model = Equipo,
    form_class = EquipoForm
    template_name = 'equipos/equipo_form.html'
    # fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion', 'estado']
    success_url = reverse_lazy('equipo-list')

# Vista para actualizar un Equipo existente
class EquipoUpdateView(UpdateView):
    model = Equipo
    template_name = 'equipos/equipo_form.html'
    fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion']
    success_url = reverse_lazy('equipo-list')

# Vista para eliminar un Equipo
class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'equipos/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo-list')

class ToggleEstadoEquipoView(View):
    def post(self, request, pk):
        equipo = get_object_or_404(Equipo, pk=pk)
        equipo.estado = not equipo.estado  # Cambiar el estado
        equipo.save()
        return redirect(reverse('equipo-list'))
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'
    def get_queryset(self):
        queryset = Usuario.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) 
            )
        return queryset

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')
class ToggleEstadoUsuarioView(View):
    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.estado = not usuario.estado  # Cambiar el estado
        usuario.save()
        return redirect(reverse('usuario-list'))
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado-list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado-list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado-list')
class ToggleEstadoEmpleadoView(View):
    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.estado = not empleado.estado  # Cambiar el estado
        empleado.save()
        return redirect(reverse('empleado-list'))
class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamos/prestamo_list.html'
    context_object_name = 'prestamos'

    def get_queryset(self):
        # Obtener la consulta GET
        query = self.request.GET.get('q', '')  # Campo de búsqueda en el formulario
        queryset = super().get_queryset()  # Obtener el queryset inicial

        # Aplicar filtro si la consulta no está vacía
        if query:
            queryset = queryset.filter(
                Q(empleado__nombre__icontains=query) |  # Filtrar por empleado
                Q(equipo__descripcion__icontains=query)  # Filtrar por equipo
            )
        return queryset

class PrestamoCreateView(CreateView):
    model = Prestamo
    form_class = PrestamoForm    
    template_name = 'prestamos/prestamo_form.html'
    # fields = ['empleado', 'equipo', 'usuario', 'fecha_prestamo', 'fecha_devolucion', 'comentario', 'estado']
    success_url = reverse_lazy('prestamo-list')

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = 'prestamos/prestamo_form.html'
    form_class = PrestamoForm       
    # fields = ['empleado', 'equipo', 'usuario', 'fecha_prestamo', 'fecha_devolucion', 'comentario', 'estado']
    success_url = reverse_lazy('prestamo-list')

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamos/prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamo-list')

class DevolverPrestamoView(UpdateView):
    model = Prestamo
    form_class = DevolverPrestamoForm
    template_name = 'prestamos/devolver_prestamo.html'
    success_url = reverse_lazy('prestamo-list')
    def form_valid(self, form):
        # Cambiar estado a devuelto
        form.instance.estado = False
        return super().form_valid(form)

def consulta_criterios_view(request):
    form = ConsultaCriteriosForm(request.GET or None)
    prestamos = Prestamo.objects.all()

    # Aplicar filtros según los criterios
    if form.is_valid():
        if form.cleaned_data.get('usuario'):
            prestamos = prestamos.filter(usuario=form.cleaned_data['usuario'])
        if form.cleaned_data.get('equipo'):
            prestamos = prestamos.filter(equipo=form.cleaned_data['equipo'])
        if form.cleaned_data.get('fecha_inicio'):
            prestamos = prestamos.filter(fecha_prestamo__gte=form.cleaned_data['fecha_inicio'])
        if form.cleaned_data.get('fecha_fin'):
            prestamos = prestamos.filter(fecha_prestamo__lte=form.cleaned_data['fecha_fin'])
        if form.cleaned_data.get('tipo_equipo'):
            prestamos = prestamos.filter(equipo__tipo_equipo=form.cleaned_data['tipo_equipo'])

    return render(request, 'prestamos/consulta_criterios.html', {'form': form, 'prestamos': prestamos})