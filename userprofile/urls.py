from django.conf.urls import url, include
from userprofile import views as userprofile_views

urlpatterns = [
    url(r'^profile/$', userprofile_views.user_profile),
    url(r'^users/$', userprofile_views.users),
    url(r'^(?P<user_id>\d+)/$', userprofile_views.user),
    url(r'^create_user/$', userprofile_views.create_user),
    url(r'^create_user_success/$', userprofile_views.create_user_success),
]
