from django.urls import path
from donasi.views import add_donasi_list, add_donasi_ajax, show_ajax, show_json, submitDonasi_ajax

app_name = 'donasi'

urlpatterns = [
    path('', show_ajax, name='show_ajax'),
    path('addDonasi/', add_donasi_list, name='add_donasi_list'),
    path('add/', add_donasi_ajax, name='add_donasi_ajax'),
    path('show-json/', show_json, name='show_json'),
    path('json/delete/<int:id>', submitDonasi_ajax, name='submitDonasi_ajax')
]