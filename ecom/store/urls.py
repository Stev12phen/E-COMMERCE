from django.urls import path
from.import views


urlpatterns= [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('register/', views.register_user, name= 'register'),
    path('product/<int:pk>/', views.product, name= 'product'),
    path('category/<str:foo>/', views.category_view, name= 'category'),
    path('admin_view/', views.admin_view, name='admin_page')

    
    
]