from django.shortcuts import render, redirect
from .models import Vacancy
from django.views import View
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# For all views regarding vacancies

# Responsible for showing all created vacancies
def vacancy_view(request):
    all_vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy.html', context={'vacancies': all_vacancies})

# Form for creation of vacancies
class VacancyForm(forms.Form):
    description = forms.CharField(max_length=1024)

# Handles creation of vacancies
class NewVacancy(View):
    def get(self, request, *args, **kwargs):
        new_vacancy = VacancyForm()
        return render(request, "vacancy/newvacancy.html", context={'vacancy_form': new_vacancy})

    # Checks if user is authenticated to create vacancies and creates a new vacancy in the model 
    def post(self, request, *args, **kwargs):
        vacancy_form = VacancyForm(request.POST)
        if (vacancy_form.is_valid()) and request.user.is_staff and request.user.is_authenticated:
            vac_data = vacancy_form.cleaned_data
            vac = Vacancy.objects.create(author=request.user, description=vac_data['description'])
            vac.save()
            return redirect('/home')

        else:
            raise PermissionDenied
