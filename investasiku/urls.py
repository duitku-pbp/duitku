from django.urls import path
from investasiku.views import *

app_name = 'investasiku'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('app/', show_app, name='show_app'),
    path('app/reksadanalist/', show_investment_all, name='show_investment_all'),
    path('app/reksadanalist/pasaruang', show_investment_pasaruang, name='show_investment_pasaruang'),
    path('app/reksadanalist/obligasi', show_investment_obligasi, name='show_investment_obligasi'),
    path('app/reksadanalist/saham', show_investment_saham, name='show_investment_saham'),
    path('json/', show_json_all, name='show_json_all'),
    path('json/pasaruang', show_json_pasaruang, name='show_json_pasaruang'),
    path('json/obligasi', show_json_obligasi, name='show_json_obligasi'),
    path('json/saham', show_json_saham, name='show_json_saham'),
    path('json/<int:id>/', show_json_id, name='show_json_id'),
    path('json/portofolio/', show_portofolio, name='show_portofolio'),
    path('add_portofolio/', add_portofolio, name='add_portofolio'),
    path('purge/', purge_portofolio, name='purge_portofolio'),

]