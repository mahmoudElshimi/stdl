from django.urls import path

from . import views


app_name = "main"

urlpatterns = [
        path("", views.index, name="index"),
        path("new/", views.new_item, name="new"),
        path("del/", views.del_item, name="del"),
        path("<str:name>", views.index, name="index"),
]
