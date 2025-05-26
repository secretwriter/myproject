from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chess/', views.chess_page, name='chess'),
    path('four/', views.four_page, name='four'),
    path('kd/', views.kd_page, name='kd'),
    path('login/', views.login_page, name='login'),
    path('ludo/', views.ludo_page, name='ludo'),
    path('logintest/', views.logintest_page, name='logintest'),
    path('more/', views.more_page, name='more'),
    path('one/', views.one_page, name='one'),
    path('options/', views.options_page, name='options'),
    path('signup/', views.signup_view, name='signup'),
    path('start/', views.start_page, name='start'),
    path('three/', views.three_page, name='three'),
    path('tic-tac-toe/', views.tic_tac_toe_page, name='tic-tac-toe'),
    path('two/', views.two_page, name='two'),
    path('five/', views.five_page, name='five'),
    path('success/', views.success_page, name='success'),
]
