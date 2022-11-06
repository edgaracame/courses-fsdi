from pyexpat import model
from django import forms
from courses.models import CATEGORY_CHOICES, Course


class CourseForm(forms.Form):
    class Meta:
        model = Course
        title = forms.CharField(max_length=256)
        subtitle = forms.CharField(max_length=256)
        body = forms.TextInput()
        category = forms.Select(choices=CATEGORY_CHOICES)
        file = forms.FileField(upload_to='documents/')
        image = forms.ImageField(upload_to='images/')
