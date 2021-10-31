from django.urls import path
from . views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('insertTag',insertTag,name='insertTag'),
    path('update/<textid>',update,name='update')
    ]