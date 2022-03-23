from django.urls import path

from . import views

app_name = "Accounting"
urlpatterns =[
    path("",views.IndexView.as_view(),name = "index"),
    path("<int:event_id>/",views.DetailView,name = "detail"),
    path("<int:event_id>/changeDB/",views.changeDB,name = "changeDB"),
    path("<int:event_id>/delete/",views.deletePay,name = "delete"),
    path("<int:event_id>/history/",views.history,name = "history"),
    path("<int:event_id>/history/delete/",views.deletePayHistory,name = "deleteInHistory"),
    path("<int:event_id>/history/search/",views.historySearch,name = "search"),
]
