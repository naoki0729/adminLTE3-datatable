from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
#    path('', views.MainView.dashboard_view, name='main'),
  path('', views.MainView.datatable_view, name='main'),
#    path('', views.MainView.myapp_list_view, name='main'),
  path('dashboard2/', views.Dash2_view, name='dashboard2'),
  path('dashboard3/', views.Dash3_view, name='dashboard3'),

]
