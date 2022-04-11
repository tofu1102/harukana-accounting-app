from django.urls import path

from . import views

app_name = "accountsetting"
urlpatterns =[
    path("<uuid:CustomUser_id>/",views.SettingView,name = "setting"),
]
