from django.urls import include, re_path
from .views import ObjetoListView, ObjetoCreateView
from .views import ObjetoUpdateView, ObjetoDeleteView


urlpatterns = [
	re_path(r'list/$', ObjetoListView.as_view(), name='objeto_list'),
	re_path(r'cad/$', ObjetoCreateView.as_view(), name='objeto_create'),
	re_path(r'(?P<pk>\d+)/$', ObjetoUpdateView.as_view(), name='objeto_update'),
	re_path(r'(?P<pk>\d+)/delete/$', ObjetoDeleteView.as_view(), name='objeto_delete'), 
]
