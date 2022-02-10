from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_watching/', views.add_watching, name='add_watching'),
    path('finches/<int:finch_id>/assoc_house/<int:house_id>/', views.assoc_house, name="assoc_house"),
    path('finches/<int:finch_id>/un_assoc_house/<int:house_id>/', views.un_assoc_house, name="un_assoc_house"),
    path('finches/<int:finch_id>/add_photo/', views.add_photo, name="add_photo"),
    path('houses/create', views.HouseCreate.as_view(), name='house_create'),
    path('houses/', views.houses_index, name='houses_index'),
    path('houses/<int:house_id>/', views.house_detail, name='house_detail'),
    path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='house_update'),
    path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='house_delete'),
]

