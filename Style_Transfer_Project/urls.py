from django.contrib import admin
from django.urls import path, include
from Style_Transfer_Application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main_page, name='show_main_page'),
    path('Transfer_Page/', include('Style_Transfer_Application.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

