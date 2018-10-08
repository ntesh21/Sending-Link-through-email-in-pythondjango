from django.urls import path, include
from django.contrib.auth import views as auth_views

from link_send import views

from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('send_mail/', views.send_mail, name='send_mail'),
    path('link_sent/', views.link_sent, name='link_sent'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
    #path('oauth', include('social_django.urls', namespace='social')),
    # path('password/',views.password, name='password'),
    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        # auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('admin/', admin.site.urls),
]
