from pyexpat import model
from django import forms
from courses.models import CATEGORY_CHOICES, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'subtitle', 'body', 'category', 'file', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subtitle'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class':'form-select'}),
        }


