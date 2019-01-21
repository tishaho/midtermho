from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/update', views.update, name='update'),
    path('<int:post_id>/comment', views.comment, name='comment'),
    path('create/', views.create, name='create'),
]
