
from django.urls import path
from . import views

urlpatterns = [
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/<int:pk>/retrieve/', views.get_note, name='get_note'),
    path('notes/', views.query_notes_by_title, name='query_notes_by_title'),
    path('notes/<int:pk>/update/', views.update_note, name='update_note'),
]
