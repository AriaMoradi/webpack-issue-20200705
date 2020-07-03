from django.views.generic import DetailView, ListView

from course.models import Course


class CourseListView(ListView):
    model = Course
    context_object_name = "course_list"


class CourseDetailView(DetailView):
    model = Course
