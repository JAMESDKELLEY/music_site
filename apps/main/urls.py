from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^music$', views.music),
    url(r'^press$', views.press),
    url(r'^upcoming_dates$', views.upcoming_dates),
    url(r'^contact_booking$', views.contact_booking),
    url(r'^subscribe$', views.subscribe),
    url(r'^subscribe2$', views.subscribe2),
    url(r'^subscribe3$', views.subscribe3),
    url(r'^subscribe4$', views.subscribe4),
    url(r'^subscribe5$', views.subscribe5),
    url(r'^subscribe6$', views.subscribe6),   
]
