from django.urls import path

from . import views

app_name = "Accounting"
urlpatterns =[
    path("",views.IndexView.as_view(),name = "index"),
    path("<int:event_id>/",views.DetailView,name = "detail"),
    path("<int:event_id>/history/",views.history,name = "history"),
]
