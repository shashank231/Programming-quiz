from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),

    path('', views.index, name='index'),
    path('languages', views.languages, name='languages'),
    path('test/<str:pk>/', views.test, name='test'),
    path('save/<str:pk>/', views.saveSelected, name='save'),
    path('result', views.result, name='result'),
    path('contactus', views.contactus, name='contact'),
]