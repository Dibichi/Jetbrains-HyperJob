from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.views import View

# For the pages that don't involve resumes or vacancies

# The default menu that is the hub for every action on the website
def menu_view(request):
    return render(request, "../templates/other/menu.html")

# A preprepared HTTP handler for handling signups
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

# Same as signups but for logins instead 
class SignInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'

# Redirects user to the right create page and non-users to 'permission denied'
class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('/vacancy/new')
            else:
                return redirect('/resume/new')
        else:
            return HttpResponse('Not authenticated')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('/vacancy/new')
            else:
                return redirect('/resume/new')
        else:
            raise PermissionDenied
