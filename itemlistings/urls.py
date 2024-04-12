"""
URL configuration for toca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('getAllItems/', views.itemListView.as_view(), name='getAllItemsPath'),
    #path('createItem/', views.itemCreateView.as_view(), name='carribean-list'),
    path('createOrder/', views.orderView.as_view(), name='order'),
    path('viewOrder/<str:name>/', views.orderViewFilterLatest.as_view(), name='orderLatestFilter'),#http://urlstuff/customer/viewOrder/Jane Doe/ Example URL for this
    path('orderItems/', views.orderItems.as_view(), name='orderitems'),
]
