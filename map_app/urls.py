from django.urls import path, include
from . import views, country_views


urlpatterns = [
    # ORGS 
    path('', views.home, name='home'),
    path('country_map/<str:id>', views.country_map, name='country_map'),
    path('add_org/', views.add_org, name='add_org'),
    path('org_details/<str:id>/', views.org_details, name='org_details'),
    path('org_update/<str:id>/', views.org_update, name='org_update'),
    path('org_delete/<str:id>/', views.org_delete, name='org_delete'),

    # COUNTRIES
    path('countries_list/', country_views.countries_list, name='countries_list'),
    path('countries_add/', country_views.countries_add, name='countries_add'),
    path('country_details/<str:id>',
         country_views.country_details, name='country_details'),
    path('country_edit/<str:id>',
         country_views.country_edit, name='country_edit'),
    path('country_delete/<str:id>',
         country_views.country_delete, name='country_delete'),

    # FOOTER AND NAVBAR LINKS
    path('imprint/', views.imprint, name='imprint'),
    path('data_policy/', views.data_policy, name='data_policy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),


]
