from django.urls import path
from . import views
from .views import PostsListView, PostsDetailView, PostsCreateView, PostsUpdateView, PostsDeleteView, UserPostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostsDetailView.as_view(), name='post-detail'),
    path('post/new/', PostsCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostsUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostsDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostsListView.as_view(), name='user-post'),
]