from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^python/$',views.python_list, name='p_list'),
    url(r'^blog/$',views.blog_list, name='pb_list'),
    url(r'^write/$',views.writeblog, name='write'),
    url(r'^(?P<id>\d+)/$',views.full_article, name='full'),
    url(r'^update/(?P<id>\d+)/$',views.update_view, name='update'),
    url(r'^delete/(?P<id>\d+)/$',views.delete_view, name='delete'),
]