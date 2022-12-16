from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('registration/', registration),
    path('about/', about),
    path('signin/', signin),
    path('result/', result),
    path('login/', student_login),
    path('change/', change_user),
    path('delete/', delete)
    # path('data/', student_data)

]
