from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('review/', views.Reviewpage, name='review'),
    path('about/', views.Aboutpage, name='about'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

