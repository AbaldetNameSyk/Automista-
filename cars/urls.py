from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('my_view/', views.my_view, name='my_view'),
    path('bmw/', views.bmw_page, name='bmw_page'),
    path('mers/', views.mers_page, name='mers_page'),
    path('volks/', views.volks_page, name='volks_page'),
    path('ren/', views.ren_page, name='ren_page'),
    path('ford/', views.ford_page, name='ford_page'),
    path('audi/', views.audi_page, name='audi_page'),
    path('sko/', views.sko_page, name='sko_page'),
    path('niss/', views.niss_page, name='niss_page'),
    path('toyo/', views.toyo_page, name='toyo_page'),
    path('hyu/', views.hyu_page, name='hyu_page'),
    path('hon/', views.hon_page, name='hon_page'),
    path('chev/', views.chev_page, name='chev_page'),
    path('maz/', views.maz_page, name='maz_page'),
    path('cit/', views.cit_page, name='cit_page'),
    path('vol/', views.vol_page, name='vol_page'),
    path('fiat/', views.fiat_page, name='fiat_page'),
    path('lex/', views.lex_page, name='lex_page'),
    path('jeep/', views.jeep_page, name='jeep_page'),
    path('lr/', views.lr_page, name='lr_page'),
    path('che/', views.che_page, name='che_page'),
    path('dac/', views.dac_page, name='dac_page'),
    path('AfterButton/', views.AfterButton_page, name='AfterButton_page'),
    path('Obrob/', views.Obrob_page, name='Obrob_page'),
]
