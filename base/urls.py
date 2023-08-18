from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('users',views.users,name="users"),
    path('profile/<str:pk>',views.UserProfile,name="profile"),
    path('author',views.author,name="author"),
    path('books/<str:pk>',views.book,name="books"),
    path('tags/<str:pk>',views.tags,name="tags"),
    path('posts',views.Posts,name="posts"),
]