from django.views.generic import DetailView, ListView

from course.models import Course
from react_mpa.views import ReactViewMixin


class CourseListView(ReactViewMixin, ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
