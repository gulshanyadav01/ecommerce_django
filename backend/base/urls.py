from django.urls import path
from .import views 
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', views.getProducts),
    path('product/<str:pk>/', views.getProduct)
]
