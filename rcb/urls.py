from django.urls import path
from rcb.views import*
app_name='b'
urlpatterns=[
    path('kingKohli/',kingKohli,name='kingKohli'),
]