from django.urls import path

from like import views

urlpatterns = [
    path('create/', views.LikeCreateView.as_view()),
    path('<int:pk>/', views.LikeDeleteView.as_view()),
    # path('', views)
]