from django.contrib import admin
from .models import Profile, Certificate, Project , Experience, Education, Skill     


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'qualification',
        'institution',
        'location',
        'start_date',
        'end_date',
        'is_current',
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'current_position',
        'years_of_experience',
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'issuing_organization',
        'issue_date',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'client',
        'role',
        'project_date',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company',
        'location',
        'start_date',
        'end_date',
        'is_current',
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'proficiency',
    )