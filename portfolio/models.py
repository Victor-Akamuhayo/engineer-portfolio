from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)

    title = models.CharField(max_length=200)

    bio = models.TextField()

    profile_photo = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    cv = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True
    )

    current_position = models.CharField(
        max_length=200,
        blank=True
    )

    years_of_experience = models.PositiveIntegerField(
        default=0
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=200
    )

    issuing_organization = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    certificate_file = models.FileField(
        upload_to='certificates/'
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    client = models.CharField(
        max_length=200,
        blank=True
    )

    role = models.CharField(
        max_length=200,
        blank=True
    )

    project_date = models.DateField(
        blank=True,
        null=True
    )

    project_image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    project_document = models.FileField(
        upload_to='project_documents/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-project_date']

    def __str__(self):
        return self.title


class Experience(models.Model):
    job_title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    is_current = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} - {self.company}"


class Education(models.Model):
    qualification = models.CharField(max_length=200)

    institution = models.CharField(max_length=200)

    location = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    end_date = models.DateField(
        blank=True,
        null=True
    )

    is_current = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.qualification} - {self.institution}"


class Skill(models.Model):
    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100,
        blank=True
    )

    proficiency = models.PositiveIntegerField(
        default=0,
        help_text="Enter a percentage from 0 to 100."
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name