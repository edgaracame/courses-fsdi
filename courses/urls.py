from django.urls import path
from courses import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name="courses_catalog"),
    path('new/', views.CourseCreateView.as_view(), name="course_new"),
    path('<int:pk>/', views.CourseDetailView.as_view(), name="course_detail"),
    path('<int:pk>/edit/', views.CourseUpdateView.as_view(), name="course_edit"),
    path('<int:pk>/delete/', views.CourseDeleteView.as_view(),
         name="course_delete"),
    path('<int:pk>/evaluation/', views.EvaluationDetailView.as_view(),
         name="course_evaluation"),
    path('programming/', views.CourseProgrammingView.as_view(),
         name="cat_programming"),
    path('digitalart/', views.CourseDigitalArtView.as_view(), name="cat_digitalart"),
    path('modeling/', views.CourseModelingView.as_view(), name="cat_modeling"),
]
