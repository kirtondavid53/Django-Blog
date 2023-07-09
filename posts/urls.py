from django.urls import path
from . import views

urlpatterns = [
          path('', views.index, name='index'),
          path('post/<str:pk>', views.post, name='post'),
          path('login', views.login_view, name='login'),
          path('add_post', views.add_post, name='add_post')
          ]