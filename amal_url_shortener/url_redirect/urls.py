from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="Dashboard"),
    path("r/<str:id>/", views.page_redirect,name="Redirect"),
    path('',views.index,name="to_dashboard"),
    path("dashboard/edit/<str:id>/", views.short_link_edit, name="Edit_shortcode"),
    path("dashboard/delete/<str:id>/", views.short_link_delete, name="Delete_shortcode"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]