from collections import namedtuple
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import formulario, mostarcolab, modColabo, deleteColaborador, uptown, form_colabor

urlpatterns = [
    path('', formulario, name="formulario"),
    path('form_colabor', form_colabor, name="form_colabor"),
    path('mostarcolab', mostarcolab, name="mostarcolab" ),
    path('modColabo/<id>', modColabo, name="modColabo"),
    path('deleteColaborador/<id>', deleteColaborador, name="deleteColaborador"),
    path('uptown', uptown, name='uptown'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)