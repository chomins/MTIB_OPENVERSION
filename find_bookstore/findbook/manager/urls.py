from django.urls import path
from . import views

urlpatterns = [
    path('manager_main/', views.manager_main, name="manager_main"),
    path('store_edit/', views.store_edit, name="store_edit"),
    path('store_update/', views.store_update, name='store_update'),
    path('manager_notice_detail/<int:notice_id>', views.manager_notice_detail, name="manager_notice_detail"),
    path('manager_notice_new/', views.manager_notice_new, name='manager_notice_new'),
    path('manager_notice_create/', views.manager_notice_create, name='manager_notice_create'),
    path('manager_notice_edit/<int:notice_id>', views.manager_notice_edit, name='manager_notice_edit'),
    path('manager_notice_update/<int:notice_id>', views.manager_notice_update, name='manager_notice_update'),
    path('manager_notice_delete/<int:notice_id>', views.manager_notice_delete, name='manager_notice_delete'),
    path('booksearch/', views.booksearch, name='booksearch'),
    path('addbook/', views.addbook, name='addbook'),
    path('deletebook/', views.deletebook, name='deletebook'),
    path('register_store/', views.register_store, name='register_store'),
    path('new_bookstore/', views.new_bookstore, name='new_bookstore'),
    path('deletebook/<int:book_id>', views.deletebook, name='deletebook'),
]