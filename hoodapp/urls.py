from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('add/bussiness/',views.add_bussiness,name = 'add-bussiness'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)