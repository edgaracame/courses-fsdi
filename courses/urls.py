from django.urls import path
from courses import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name="courses_catalog"),
    path('new/', views.CourseCreateView.as_view(), name="course_new"),
    path('<int:pk>/', views.CourseDetailView.as_view(), name="course_detail"),
    path('<int:pk>/edit/', views.CourseUpdateView.as_view(), name="course_edit"),
    path('<int:pk>/delete/', views.CourseDeleteView.as_view(),
         name="article_delete"),
]
