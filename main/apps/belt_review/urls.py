from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),  
    url(r'^process$', views.register),
    url(r'^signIn$', views.signIn),
    url(r'^books$', views.books),
    url(r'^books/add/(?P<num>\d+)$', views.add_books),
    url(r'^book/added/(?P<num>\d+)$', views.add),
    url(r'^books/(?P<num>\d+)$', views.current_book),
    url(r'^books/display$', views.display_book),
    url(r'^add_review/(?P<uid>\d+)/(?P<bid>\d+)$', views.add_review),
    url(r'^user_info/(?P<num>\d+)$', views.user_info),
    url(r'^signOut$', views.signOut),
]
