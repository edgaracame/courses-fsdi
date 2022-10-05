from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Course


class CourseListView(ListView):
    template_name = "courses/catalog.html"
    model = Course


class CourseDetailView(DetailView):
    template_name = "courses/course.html"
    model = Course


class CourseCreateView(CreateView):
    template_name = "courses/add.html"
    model = Course
    fields = ["title", "subtitle", "body", "category", "file", "image"]
    success_url = reverse_lazy("courses_catalog")


class CourseUpdateView(UpdateView):
    template_name = "courses/edit.html"
    model = Course
    fields = ["title", "subtitle", "body", "category", "file", "image"]
    success_url = reverse_lazy("courses_catalog")

    def test_func(self):
        obj = self.get_object()


class CourseDeleteView(DeleteView):
    template_name = "courses/delete.html"
    model = Course
    success_url = reverse_lazy("courses_catalog")

    def test_func(self):
        obj = self.get_object()
