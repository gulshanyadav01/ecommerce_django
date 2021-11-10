from django.urls import path
from base.views import order_views as views 

urlpatterns = [
    path('add/', views.addOrderItems),
    path("<str:pk>/", views.getOrderById, name = "order by id"),
    path("<str:pk>/pay", views.updateOrderToPaid, name = 'pay'),
    
]
