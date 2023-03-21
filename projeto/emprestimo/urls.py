from django.urls import include, re_path

from .views import EmprestimoListView, EmprestimoCreateView
from .views import EmprestimoUpdateView, EmprestimoDeleteView


urlpatterns = [
	re_path(r'list/$', EmprestimoListView.as_view(), name='emprestimo_list'),
	re_path(r'cad/$', EmprestimoCreateView.as_view(), name='emprestimo_create'),
	re_path(r'(?P<pk>\d+)/$', EmprestimoUpdateView.as_view(), name='emprestimo_update'),
	re_path(r'(?P<pk>\d+)/delete/$', EmprestimoDeleteView.as_view(), name='emprestimo_delete'), 
]
