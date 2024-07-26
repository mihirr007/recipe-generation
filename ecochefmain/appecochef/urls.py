from django.urls import path
from . import views
from .views import HomeView, SignupView, LoginView
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('screen1/', views.screen1, name='screen1'),
    path('screen2/', views.screen2, name='screen2'),
    path('screen3/', views.screen3, name='screen3'),
    path('screen4/', views.screen4, name='screen4'),
    path('try-now/', views.try_now_view, name='try_now'),
    path('logout/', views.logout_view, name='logout'),
    
]


