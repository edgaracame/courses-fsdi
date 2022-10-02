from django.db import models
from django.forms import ModelForm
from django.urls import reverse

CATEGORY_CHOICES = (
    ("programming", "Programming"),
    ("digital art", "Digital Art"),
    ("modeling", "Modeling"),
)


class Course(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    category = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default='programming'
    )
    file = models.FileField(upload_to='documents/', default=None)
    image = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", args=[self.id])


class CourseForm(ModelForm):
    model = Course
    fields = ["title", "subtitle", "body", "category", "file", "image"]
