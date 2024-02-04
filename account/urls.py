from django.urls import path
from .views import account, cancel_subscription, reactivate_subscription

urlpatterns = [
    path('', account, name='account'),
    path('cancel/(?P<subscription_id>[0-9A-Za-z_]+)$', cancel_subscription, name='cancel_subscription'),
    path('reactivate/(?P<subscription_id>[0-9A-Za-z_]+)$', reactivate_subscription, name='reactivate_subscription')]