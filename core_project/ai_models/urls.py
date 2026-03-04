from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AiModelListView.as_view(), name='ai_list'),
    path('new/', views.AiModelCreateView.as_view(), name='ai_create'),
    path('<int:pk>/edit/', views.AiModelUpdateView.as_view(), name='ai_update'),
    path('<int:pk>/delete/', views.AiModelDeleteView.as_view(), name='ai_delete'),
]