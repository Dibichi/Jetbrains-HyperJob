"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from hyperjob.views import menu_view, SignInView, SignupView, HomeView
from vacancy.views import vacancy_view, NewVacancy
from resume.views import resume_view, NewResume
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_view),
    path('vacancies/', vacancy_view),
    path('resumes/', resume_view),
    path('login/', RedirectView.as_view(url='/login')),
    path('login', SignInView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', SignupView.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
    path('home', HomeView.as_view()),
    path('vacancy/new/', RedirectView.as_view(url='/vacancy/new')),
    path('vacancy/new', NewVacancy.as_view()),
    path('resume/new/', RedirectView.as_view(url='/resume/new')),
    path('resume/new', NewResume.as_view()),
]

