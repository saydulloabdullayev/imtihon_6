from django.urls import path
from . import views

urlpatterns = [
    path('', views.salib_list, name='salib_list'),
    path('themes/', views.theme_list, name='theme_list'),
    path('create/', views.theme_create, name='theme_create'),
    path('<int:pk>/', views.theme_detail, name='theme_detail'),
    path('<int:pk>/update/', views.theme_update, name='theme_update'),
    path('<int:pk>/delete/', views.theme_delete, name='theme_delete'),
    path('salib_bir/', views.salib_bir, name= 'salib_bir'),
    path('salib_ikki/', views.salib_ikki, name ='salib_ikki'),
    path('salib_uch/', views.salib_uch, name= 'salib_uch'),
    path('salib_umumiy/', views.salib_umumiy, name ='salib_umumiy'),

]
