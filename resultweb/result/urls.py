from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('quizzle', quizzle, name='quizzle'),
    path('yds', yds, name='yds'),
    path('itmanager', itmanager, name='itmanager'),
    path('sql', sql, name='sql'),
    path('datashark', datashark, name='datashark'),
    path('ciphertrail', cipher, name='ciphertrail'),
    path('mobilelegends', mobile, name='mobilelegends'),
]