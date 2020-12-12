from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('se',views.se,name='se'),
    path('ml',views.ml,name='ml'),
    path('daa',views.daa,name='daa'),
    path('cn',views.cn,name='cn'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('submission',views.submission,name='submission')
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)