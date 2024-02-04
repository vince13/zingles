from django.urls import path, include
from chat.views import chat, new_message_check, wink, chat_ajax, chat_home, read_messages, winks, read_wink, read_view, views, reject

urlpatterns = [
    path('(?P<id>\d+)', chat, name="chat"),
    path('home/', chat_home, name="chat_home"),
    path('ajax/winks/', wink, name="wink"),
    path('ajax/reject/', reject, name="reject"),
    path('ajax/new_message_check/', new_message_check, name='new_message_check'),
    path('ajax/read/', read_messages, name="read_messages"),
    path('ajax/new_message/', chat_ajax, name="new_message"),
    path('winks/', winks, name="winks"),
    path('views/', views, name="views"),
    path('ajax/read-view/', read_view, name='read_view'),
    path('ajax/read-wink/', read_wink, name='read_wink'),
]


# from django.conf.urls import url, include
# from profiles.views import index, logout, login, register, user_profile, create_profile, validate_username
# from profiles import url_reset


# urlpatterns = [
#     url(r'^$', view_cart, name="view_cart"),
#     url(r'^add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
#     url(r'^adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart")
#     ]