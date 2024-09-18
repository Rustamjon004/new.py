
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),  # Asosiy sahifa
    path('users/', views.users_page, name='users_page'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
]