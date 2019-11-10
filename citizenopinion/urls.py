from django.conf.urls import url
from django.urls import path

from . import views

app_name = "citizenopinion"
urlpatterns = [
    path('<city>', views.FilterCity.as_view(), name='filter_index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
