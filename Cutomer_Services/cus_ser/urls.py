from django.urls import path
from . import views


urlpatterns = [
    path('main', views.main, name="main"),
    path('', views.home, name="home"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('products/', views.products, name="products"),
    path('customers/<str:pk>', views.customers, name="customers"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
