from django.urls import path

from . import views


urlpatterns = [
    path('partner/', views.partner_register, name='mip-partner')
]