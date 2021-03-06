from django.conf.urls import url
from django.contrib.auth import views as auth_views

from currency.views import CustomPasswordResetView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', auth_views.login, {'redirect_authenticated_user': True }, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_reset/$', CustomPasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^user/$', views.UserListView.as_view(), name='users_list'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', views.PasswordUpdateView.as_view(), name='edit_user'),
    url(r'^user/edit/$', views.edit_profile, name='edit_user_profile'),
    url(r'^user/edit/password/$', views.profile_password, name='profile_password'),

    url(r'^register/(?P<pk>[0-9a-f-]+)/$', views.preregister, name='preregister'),
    url(r'^register/success/$', views.preregister_success, name='preregister_success'),

    url(r'^map/$', views.entity_map, name='map'),
    url(r'^entity/$', views.user_entity, name='user_entity'),
    url(r'^entity/add$', views.add_entity, name='add_entity'),
    url(r'^qr/(?P<pk>[0-9a-f-]+)/$', views.entity_detail, name='entity_qr_detail'),
    url(r'^entity/(?P<pk>[0-9a-f-]+)/$', views.entity_detail, name='entity_detail'),
    url(r'^entity/(?P<pk>[0-9a-f-]+)/edit/$', views.entity_edit, name='entity_edit'),
    #url(r'^entities/$', views.entity_list, name='entity_list'),
    url(r'^entities/$', views.EntityListView.as_view(), name='entity_list'),

    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^profile/admin/$', views.ProfileListView.as_view(), name='profile_list'),

    url(r'^profile/(?P<pk>[0-9a-f-]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/(?P<pk>[0-9a-f-]+)/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^users/search/$', views.search_users, name='search_users'),

    url(r'^categories/$', views.category_list, name='category_list'),
    url(r'^categories/add$', views.add_category, name='add_category'),
    url(r'^categories/(?P<pk>[0-9a-f-]+)/edit/$', views.category_edit, name='category_edit'),

    url(r'^dashboard/$', views.profile, name='dashboard'),
]