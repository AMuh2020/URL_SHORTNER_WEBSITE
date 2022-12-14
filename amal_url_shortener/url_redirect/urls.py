from django.urls import path

from . import views

urlpatterns = [
    path("redirect/dashboard/", views.dashboard, name="Dashboard"),
    path("r/<str:id>/", views.page_redirect,name="Redirect"),
    path('',views.go,name="Redirect"),
    path("redirect/dashboard/edit/<str:id>/", views.short_link_edit, name="Edit_shortcode"),

]