from django.urls import path

from . import views

app_name = "Accounting"
urlpatterns =[
    path("",views.IndexView.as_view(),name = "index"),
    path("<uuid:event_id>/",views.DetailView,name = "detail"),
    path("<uuid:event_id>/history/",views.history,name = "history"),
    path("createEvent/",views.createEvent,name = "createEvent"),
]
