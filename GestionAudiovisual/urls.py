"""
URL configuration for GestionAudiovisual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from GestionAudiovisualApp.views import ( ToggleEstadoEmpleadoView, ToggleEstadoEquipoView, ToggleEstadoModeloView, ToggleEstadoTecnologiaConexionView, ToggleEstadoUsuarioView, inicio,TipoEquipoListView, TipoEquipoCreateView, TipoEquipoUpdateView, TipoEquipoDeleteView,ToggleEstadoTipoEquipoView,                                         
    MarcaListView, MarcaCreateView, MarcaUpdateView, MarcaDeleteView, ToggleEstadoMarcaView,
    ModeloListView, ModeloCreateView, ModeloUpdateView, ModeloDeleteView,
    TecnologiaConexionListView, TecnologiaConexionCreateView, TecnologiaConexionUpdateView, TecnologiaConexionDeleteView,
    EquipoListView, EquipoCreateView, EquipoUpdateView, EquipoDeleteView,
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView,
    PrestamoListView, PrestamoCreateView, PrestamoUpdateView, PrestamoDeleteView, DevolverPrestamoView, CustomLoginView, consulta_criterios_view, consulta_imprimir_view, consulta_exportar_excel_view, dashboard_view
)
from GestionAudiovisualApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', dashboard_view, name='inicio'),  
    path('', CustomLoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('tipos/', TipoEquipoListView.as_view(), name='tipoequipo-list'),
    path('tipos/new/', TipoEquipoCreateView.as_view(), name='tipoequipo-create'),
    path('tipos/edit/<int:pk>/', TipoEquipoUpdateView.as_view(), name='tipoequipo-update'),
    path('tipos/delete/<int:pk>/', TipoEquipoDeleteView.as_view(), name='tipoequipo-delete'),
    path('tipoequipos/<int:pk>/toggle_estado/', ToggleEstadoTipoEquipoView.as_view(), name='tipoequipo-toggle-estado'),


      # CRUD de Marca
    path('marcas/', MarcaListView.as_view(), name='marca-list'),
    path('marcas/new/', MarcaCreateView.as_view(), name='marca-create'),
    path('marcas/update/<int:pk>/', MarcaUpdateView.as_view(), name='marca-update'),
    path('marcas/delete/<int:pk>/', MarcaDeleteView.as_view(), name='marca-delete'),
    path('marcas/<int:pk>/toggle_estado/', ToggleEstadoMarcaView.as_view(), name='marca-toggle-estado'),


    # CRUD de Modelo
    path('modelos/', ModeloListView.as_view(), name='modelo-list'),
    path('modelos/new/', ModeloCreateView.as_view(), name='modelo-create'),
    path('modelos/update/<int:pk>/', ModeloUpdateView.as_view(), name='modelo-update'),
    path('modelos/delete/<int:pk>/', ModeloDeleteView.as_view(), name='modelo-delete'),
    path('modelos/<int:pk>/toggle_estado/', ToggleEstadoModeloView.as_view(), name='modelo-toggle-estado'),

    # CRUD de Tecnología de Conexión
    path('tecnologias/', TecnologiaConexionListView.as_view(), name='tecnologiaconexion-list'),
    path('tecnologias/new/', TecnologiaConexionCreateView.as_view(), name='tecnologiaconexion-create'),
    path('tecnologias/update/<int:pk>/', TecnologiaConexionUpdateView.as_view(), name='tecnologiaconexion-update'),
    path('tecnologias/delete/<int:pk>/', TecnologiaConexionDeleteView.as_view(), name='tecnologiaconexion-delete'),
    path('tecnologias/<int:pk>/toggle_estado/', ToggleEstadoTecnologiaConexionView.as_view(), name='tecnologiaconexion-toggle-estado'),


    # CRUD de Equipos
    path('equipos/', EquipoListView.as_view(), name='equipo-list'),
    path('equipos/new/', EquipoCreateView.as_view(), name='equipo-create'),
    path('equipos/<int:pk>/edit/', EquipoUpdateView.as_view(), name='equipo-update'),
    path('equipos/<int:pk>/delete/', EquipoDeleteView.as_view(), name='equipo-delete'),
    path('equipos/<int:pk>/toggle_estado/', ToggleEstadoEquipoView.as_view(), name='equipo-toggle-estado'),

    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/new/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/edit/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<int:pk>/delete/', UsuarioDeleteView.as_view(), name='usuario-delete'),
    path('usuarios/<int:pk>/toggle_estado/', ToggleEstadoUsuarioView.as_view(), name='usuario-toggle-estado'),

    path('empleados/', EmpleadoListView.as_view(), name='empleado-list'),
    path('empleados/new/', EmpleadoCreateView.as_view(), name='empleado-create'),
    path('empleados/<int:pk>/edit/', EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('empleados/<int:pk>/delete/', EmpleadoDeleteView.as_view(), name='empleado-delete'),
    path('empleados/<int:pk>/toggle_estado/', ToggleEstadoEmpleadoView.as_view(), name='empleado-toggle-estado'),

    path('prestamos/', PrestamoListView.as_view(), name='prestamo-list'),
    path('prestamos/new/', PrestamoCreateView.as_view(), name='prestamo-create'),
    path('prestamos/<int:pk>/edit/', PrestamoUpdateView.as_view(), name='prestamo-update'),
    path('prestamos/<int:pk>/delete/', PrestamoDeleteView.as_view(), name='prestamo-delete'),
    path('prestamos/<int:pk>/devolver/', DevolverPrestamoView.as_view(), name='devolver-prestamo'),
    path('consulta/', consulta_criterios_view, name='consulta-criterios'),
    path('consulta/imprimir/', consulta_imprimir_view, name='consulta-imprimir'),
    path('consulta/exportar-excel/', consulta_exportar_excel_view, name='consulta-exportar-excel'),

]
