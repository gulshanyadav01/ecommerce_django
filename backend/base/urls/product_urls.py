from django.urls import path
from base.views import product_views as  views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

urlpatterns = [
    
    path('', views.getProducts),
    path('<str:pk>/', views.getProduct),

]
