from django.urls import path
from base.views import user_views as views 
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.registerUser), 

    path('profile/', views.getUserProfile),

    path('profile/update/', views.updateUserProfile),

    path("", views.getUsers, name = "users"),
]
