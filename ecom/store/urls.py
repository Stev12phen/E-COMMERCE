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
    path('admins_page/', views.admins_page, name='admins_page'),
    path('add_product/', views.add_product, name= 'add_product'),
    
    

    
    
]