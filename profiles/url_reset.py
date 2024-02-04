from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="userauths/password_reset.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("reset/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # url(', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    # url('done/$', password_reset_done, name='password_reset_done'),
    # url('(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    #     {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    # url('complete/$', password_reset_complete, name="password_reset_complete")
]
