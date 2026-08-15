from django.shortcuts import render
from .models import Profile, Certificate, Project, Experience, Education, Skill 

    
def home(request):
    profile = Profile.objects.first()
    certificates = Certificate.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'profile': profile,
        'certificates': certificates,
        'experiences': experiences,
        'education': education,
        'projects': projects,
        'skills': skills,
    }

    return render(
        request,
        'portfolio/home.html',
        context
    )