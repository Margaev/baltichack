from django.urls import path
from .views import home_page
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
]
