"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from festival.views import submit, success_view, login_page, main_page, login, result, reset, get_vote_results_api
import atexit
from django.db import connections

urlpatterns = [
    path('submit/', submit, name='submit'),
    path('success/', success_view, name= 'success_view'),
    path('loginpage/', login_page, name= 'login_page'),
    path('mainpage/', main_page, name= 'main_page'),
    path('login/', login, name= 'login'),
    path('result/', result, name= 'result'),
    path('reset/', reset, name='reset'),
    path('api/vote-results/',get_vote_results_api,name='get_vote_results_api')
]

@atexit.register
def cleanup():
    for conn in connections.all():
        conn.close()