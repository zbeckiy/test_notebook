from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('generate_uuid/<int:pk>/', views.generate_uuid, name='generate_uuid'),
    path('delete_uuid/<int:pk>/', views.delete_uuid, name='delete_uuid'),
    path('note/<uuid:note_uuid>/', views.note_detail_uuid, name='note_detail_uuid'),
]
