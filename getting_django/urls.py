"""getting_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include 
from testgateway.views import questionView, questionFilterView, questionSubmitView
from django.contrib.auth import views as auth_views
from account.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testgateway/', include('testgateway.urls'), name = "test_view"),
    path('test/', questionView, name = "question_view"),
    path('fq/', questionFilterView , name = "question_filter"),
    path('xyz/', questionSubmitView , name = "question_submit"),
    # path('login/', auth_views.LoginView.as_view(), name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name = "registration/logged_out.html"), name = 'logout'),
    # path('', dashboard, name = 'dashboard'),
    # path('account/', include('account.urls'), name = 'account'),
    path('users/', include('users.urls'), name = 'users'),
]
