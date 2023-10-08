from django.urls import path
from work1app import views

urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),
    
    #CRUD
    path('create/', views.create,name='create'),
    path('search/', views.Search.as_view(),name='search'),
    # path('search_count/',views.SearchCount.as_view(),name='search_count'),
    path('update/<str:pk>/', views.update,name='update'),
    path('delete/<str:pk>/', views.delete,name='delete'),
    path('readAll/', views.readAll,name='readAll'),

]


