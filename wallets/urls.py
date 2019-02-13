from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^payments/$', views.pending_payments, name='pending_payments'),
    url(r'^payments/new$', views.new_payment, name='new_payment'),
    url(r'^payments/admin$', views.admin_payments, name='admin_payments'),
    url(r'^payments/(?P<pk>[0-9a-f-]+)/$', views.payment_detail, name='payment_detail'),

    url(r'^wallet/$', views.user_wallet, name='user_wallet'),
    url(r'^wallet/types$', views.wallet_types_list, name='wallet_types_list'),
    url(r'^transactions/$', views.transaction_list, name='transaction_list'),

]