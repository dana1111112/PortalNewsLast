from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('my-articles/', views.my_articles, name='my_articles'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    
    path('moderator/', views.moderator_dashboard, name='moderator_dashboard'),
    path('moderator/approve/<int:article_id>/', views.approve_article, name='approve_article'),
    path('moderator/reject/<int:article_id>/', views.reject_article, name='reject_article'),
    path('moderator/delete/<int:article_id>/', views.delete_article_admin, name='delete_article_admin'),
    
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('<slug:slug>/edit/', views.article_edit, name='article_edit'),
    path('<slug:slug>/like/', views.toggle_like, name='toggle_like'),
]