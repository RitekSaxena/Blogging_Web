from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= 'home'),
    path('detail/<int:pk>', views.detail, name = 'detail'),
    path('detail/upvote/<int:pk>/<int:comm_id>', views.upvote, name='upvote')
]