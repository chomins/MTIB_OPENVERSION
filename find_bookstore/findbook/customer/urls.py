
from django.urls import path
from . import views

urlpatterns = [
    path('customer_notice/<int:bookstore_id>/', views.notice,name="customer_notice"),
    path('customer_review/<int:bookstore_id>/', views.review,name="customer_review"),
    path('customer_review_add/<int:bookstore_id>/',views.review_add,name="customer_review_add"),
    path('customer_review_del/<int:bookstore_id>/',views.review_del,name="customer_review_del"),
    # # path('customer_review/commenting',views.review,name="customer_review_commenting"),
]