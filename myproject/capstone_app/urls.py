from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_page, name='success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin login and dashboard
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Game pages
    path('chess/', views.chess_page, name='chess'),
    path('ludo/', views.ludo_page, name='ludo'),
    path('four/', views.four_page, name='four'),
    path('five/', views.five_page, name='five'),
    path('three/', views.three_page, name='three'),
    path('two/', views.two_page, name='two'),
    path('one/', views.one_page, name='one'),
    path('tic-tac-toe/', views.tic_tac_toe_page, name='tic_tac_toe'),
    path('kd/', views.kd_page, name='kd'),
    path('more/', views.more_page, name='more'),
    path('options/', views.options_page, name='options'),
    path('start/', views.start_page, name='start'),
    path('logintest/', views.logintest_page, name='logintest'),
    path ('chatbox/', views.chatbox_page, name='chatbot'),
    # Admin Dashboard APIs
    path('api/admin/total-users/', views.total_users, name='total_users'),
    path('api/admin/total-games/', views.total_games, name='total_games'),
    path('api/admin/pending-requests/', views.pending_requests, name='pending_requests'),
]
