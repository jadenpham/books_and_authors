from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^book_info/(?P<book_id>\d+)$', views.book_info),
    url(r'^book_info/(?P<book_id>\d+)/add_author$', views.add_author),
    url(r'^authors$', views.all_authors),
    url(r'^new_author$', views.new_author),
    url(r'^authors/(?P<author_id>\d+)$', views.author_info),
    url(r'^authors/(?P<author_id>\d+)/book_to_author$', views.book_to_author)

]