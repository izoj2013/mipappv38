from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='mip-home'),
    path('team/', views.team, name='mip-team'),
    path('partnership/', views.partnership, name='mip-partner'),
    path('csi-jump/', views.csi_jump, name='mip-csi-jump'),
    path('research/', views.research, name='mip-research'),
    path('iac-stds', views.home, name='mip-iac'),
    path('lifelinenets', views.home, name='mip-lln'),
    path('donor/', views.donor, name='mip-donor'),
]