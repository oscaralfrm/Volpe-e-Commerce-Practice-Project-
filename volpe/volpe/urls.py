from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registrarse/', views.registration_page, name="registrarse"),
    path('conectarse/', views.login_page, name="conectarse"),
    path('mi-cuenta/', views.account, name="mi-cuenta"),
    path('tienda/', views.shop, name="tienda"),
    path('mi-carrito/', views.cart, name="mi-carrito"),
    path('acerca-de-nosotros/', views.about_us, name="acerca-de-nosotros"),
    path('contacto/', views.contact, name="contacto"),
]

handler404 = 'volpe.views.error_page'