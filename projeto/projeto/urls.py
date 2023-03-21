from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('core.urls')),
    re_path(r'emprestimo/', include('emprestimo.urls')),
    re_path(r'objeto/', include('objeto.urls')),
    re_path(r'usuario/', include('usuario.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)    