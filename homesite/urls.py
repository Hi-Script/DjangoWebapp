from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('review/', views.Reviewpage, name='review'),
    path('about/', views.Aboutpage, name='about'),
    path('contact/', views.ContactPage, name='contact'),
    path('blog/<str:pk>/', views.getblogPost, name='blogdetail'),
    path('blog/', views.Blogs, name='blog' ),
    path('sucess/', views.Response, name='success' ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

