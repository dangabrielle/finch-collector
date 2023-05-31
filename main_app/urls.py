from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('finches/', views.finch_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='detail')
]
