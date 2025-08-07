
from django.urls import path
from . import views

urlpatterns = [
	# Define your URL patterns here
	path('', views.home, name='home'),
	path('news/', views.news_list, name='news_list'),
	path('players/', views.player_list, name='player_list'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('news/<int:news_id>/', views.news_detail, name='news_detail'),
	path('players/<int:player_id>/', views.player_detail, name='player_detail'),
]