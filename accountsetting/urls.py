from django.urls import path

from . import views

app_name = "accountsetting"
urlpatterns =[
    path("",views.SettingView,name = "setting"),
    path("makefriends/",views.friend,name = "friend"),
]
