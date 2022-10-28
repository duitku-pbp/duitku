from django.urls import path
from investasiku.views import *

app_name = 'investasiku'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('app/', show_app, name='show_app'),
    path('json/', show_json, name='show_json'),
    path('app/pasaruang/', show_pasaruang, name='show_pasaruang'),
    path('app/obligasi/', show_obligasi, name='show_obligasi'),
    path('app/saham/', show_saham, name='show_saham'),
]