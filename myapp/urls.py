from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^showprofile/$',views.showProfile, name='showprofile'),
    url(r'^deleteprofile/(?P<id>\d+)/$',views.deleteProfile, name='deleteprofile'),
    url(r'^editprofile/$',views.editProfile, name='editprofile'),
    url(r'^change-password/$',views.changepass, name='changepass'),
]