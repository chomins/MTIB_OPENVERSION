from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .models import *

urlpatterns = [
    path('', views.before_sign, name="before_sign"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("c_register/", views.c_register, name="c_register"),
    path("m_register/", views.m_register, name="m_register"),
    path("sign_up_check/",views.sign_up_check, name="sign_up_check"),
    path("before_psy/", views.before_psy, name="before_psy"),
    path("sign_psy/", views.sign_psy, name="sign_psy"),
    path("before_search/", views.before_search, name="before_search"),
    path("recovery_id/", views.recovery_id, name="recovery_id"),
    path("recovery_id/find/", views.ajax_find_id_view, name="ajax_find_id_view"),
    path('recovery_pw/', views.recovery_pw, name='recovery_pw'),
    path('recovery_pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
    path('recovery_pw/auth/', views.auth_confirm_view, name='recovery_auth'),
    path('reset_pw/', views.auth_pw_reset_view, name='reset_pw'),
    path("sign_psy2/", views.sign_psy2, name="sign_psy2"),
    path("sign_psy2_1/", views.sign_psy2_1, name="sign_psy2_1"),
    path("sign_psy2_2/", views.sign_psy2_2, name="sign_psy2_2"),
    path("sign_psy2_3/", views.sign_psy2_3, name="sign_psy2_3"),
    path("sign_psy3/", views.sign_psy3, name="sign_psy3"),
    path("sign_psy3_1/", views.sign_psy3_1, name="sign_psy3_1"),
    path("sign_psy3_2/", views.sign_psy3_2, name="sign_psy3_2"),
    path("sign_psy3_3/", views.sign_psy3_3, name="sign_psy3_3"),
    path("tag_comfort/", views.tag_comfort, name="tag_comfort"),
    path("tag_enjoy/", views.tag_enjoy, name="tag_enjoy"),
    path("tag_cool/", views.tag_cool, name="tag_cool"),
    path("tag_simple/", views.tag_simple, name="tag_simple"),
    path('recommend_store/', views.recommend_store, name="recommend_store"),
    path('',include('manager.urls')),
    path('',include('customer.urls')),
]