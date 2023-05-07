from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoListCreateApiView.as_view()),
    path('<int:pk>/update/', views.ProdutoUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProdutoDestroyAPIView.as_view()),
    path('<int:pk>/', views.ProdutoDetailAPIView.as_view()),
]
