from django.urls import include, re_path

from .views import UsuarioListView, UsuarioCreateView
from .views import UsuarioUpdateView, UsuarioDeleteView
from .views import UsuarioRegisterView, UsuarioRegisterSuccessView, UsuarioRegisterActivateView

urlpatterns = [
	re_path(r'list/$', UsuarioListView.as_view(), name='usuario_list'),
	re_path(r'cad/$', UsuarioCreateView.as_view(), name='usuario_create'),
	re_path(r'(?P<pk>\d+)/$', UsuarioUpdateView.as_view(), name='usuario_update'),
	re_path(r'(?P<pk>\d+)/delete/$', UsuarioDeleteView.as_view(), name='usuario_delete'),
	re_path(r'register/success/',UsuarioRegisterSuccessView.as_view(),name='usuario_register_success'),
	re_path(r'register/(?P<slug>[-\w\d]+)/activate/', UsuarioRegisterActivateView.as_view(), name='usuario_register_activate'),
	re_path(r'register', UsuarioRegisterView.as_view(), name='usuario_register'), 
]