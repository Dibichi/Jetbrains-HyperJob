from django.shortcuts import render, redirect
from .models import Resume
from django import forms
from django.views import View
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# For all views regarding resumes

# Responsible for showing all created resumes
def resume_view(request):
    all_resumes = Resume.objects.all()
    return render(request, 'resume/resume.html', context={'resumes': all_resumes})

# Form for creation of resumes
class ResumeForm(forms.Form):
    description = forms.CharField(max_length=1024)

# Handles creation of resumes
class NewResume(View):
    def get(self, request, *args, **kwargs):
        new_resume = ResumeForm()
        return render(request, "resume/newresume.html", context={'resume_form': new_resume})

    # Checks if user is authenticated to create resumes and creates a new resume in the model 
    def post(self, request, *args, **kwargs):
        resume_form = ResumeForm(request.POST)
        if (resume_form.is_valid()) and (request.user.is_staff is False) and request.user.is_authenticated:
            resume_data = resume_form.cleaned_data
            res = Resume.objects.create(author=request.user, description=resume_data['description'])
            res.save()
            return redirect('/home')

        else:
            raise PermissionDenied
