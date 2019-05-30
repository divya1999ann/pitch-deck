from django.contrib import admin

from django.urls import path
from pitch import views
urlpatterns = [path('',views.blank),
               path('home/',views.home),
               path('register/',views.register),
               path('login/',views.user_login),
               path("input/",views.input),
               path('submit/',views.create),
               path('logout/',views.user_logout)

]
