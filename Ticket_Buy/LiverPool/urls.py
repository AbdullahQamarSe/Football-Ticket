from django.contrib import admin
from django.urls import path,include
from LiverPool import views

urlpatterns = [
    path("", views.Liver_pool, name="Liver_pool"),
    path("Stop_pool", views.Stop_pool, name="Stop_pool"),
    path("Liver_pool_Sel", views.Ticket_Selenium, name="Liver_pool_Sel"),
]
