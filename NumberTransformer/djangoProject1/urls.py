from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jisuan/', views.calculate),
    path('getdata/', views.show)
]