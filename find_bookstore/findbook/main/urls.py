
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('mypage',views.mypage,name="mypage"),
    path('map',views.map,name="map"),
    path('subscription',views.subscription,name="subscription"),
    path('tag_result',views.tag_result,name="tag_result"),
    path('customer_info',views.customer_info,name="customer_info"),
    path('my_reply',views.customer_info,name="my_reply"),
    path('add_complain',views.add_complain,name="add_complain"),
    path('serach_bookstore', views.serach_bookstore, name="serach_bookstore"),
]