from django.urls import path

from course.views import CourseListView, CourseDetailView

urlpatterns = [
    path("", CourseListView.as_view()),
    path("<slug:slug>/", CourseDetailView.as_view())
]