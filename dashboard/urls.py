from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
#    path('', views.MainView.dashboard_view, name='main'),
   path('', views.MainView.datatable_view, name='main'),
#    path('', views.MainView.myapp_list_view, name='main'),
]
