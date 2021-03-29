from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('detail_dv/<str:pk_donvi>/', views.detail_DV, name='detail_dv'),
    path('create_dv', views.create_DV, name='create_dv'),
    path('save_dv', views.save_DV, name='save_dv'),
    path('update_dv/<int:id>', views.update_DV, name='update_dv'),
    path('del_dv/<int:id>', views.del_DV, name='del_dv'),
    path('save_del_dv/<int:id>', views.save_del_DV, name='save_del_dv'),
    # Cong Doan Vien #
    path('create_cdv', views.create_CDV, name='create_cdv'),
    path('save_cdv', views.save_CDV, name='save_cdv'),
    path('del_cdv/<int:id>', views.del_CDV, name='del_cdv'),
    path('save_del_cdv/<int:id>', views.save_del_CDV, name='save_del_cdv'),
    path('update_cdv/<int:id>', views.update_CDV, name='update_cdv'),
    path('create_tour', views.create_tour, name='create_tour'),
    path('save_tour', views.save_tour, name='save_tour'),
    path('detail_tour/<int:id>/', views.detail_tour, name='detail_tour'),
    path('del_tour/<int:id>', views.del_tour, name='del_tour'),
    path('save_del_tour/<int:id>', views.save_del_tour, name='save_del_tour'),
    path('update_tour/<int:id>', views.update_Tour, name='update_tour'),
    path('cdv', views.CDV, name='cdv'),
    path('tour', views.tour, name='tour'),
    path('register_tour', views.register_tour, name='register_tour'),
    path('save_register', views.save_register, name='save_register'),
    path('del_DKTour/<int:id>', views.del_dktour, name='del_dktour'),
    path('save_del_DKtour/<int:id>', views.save_del_DKtour, name='save_del_DKtour'),
    #################################
    path('', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('registerAccount', views.register_Account, name='registerAccount')
]