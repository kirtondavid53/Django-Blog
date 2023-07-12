from django.urls import path
from . import views

urlpatterns = [
          path('', views.index, name='index'),
          path('post/<str:pk>', views.post, name='post'),
          path('login', views.login_view, name='login'),
          path('register', views.register_view, name='register'),
          path('logout', views.logout_view, name='logout'),
          path('add_post', views.add_post, name='add_post'),
          path('update_post/<int:pk>', views.update_post, name='update_post'),
          path('delete_post/<int:pk>', views.delete_post, name='delete_post')
          ]