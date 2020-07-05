import genericpath
import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import DetailView, ListView

from course.models import Course


class JSMixin:
    def get_bundle_path(self):
        return genericpath._splitext(self.get_template_names()[0], '\\', '/', '.')[0] + ".js"

    context_object_name = "react_props"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print("fuck")
        # context[self.context_object_name] = json.dumps(list(context[self.context_object_name]), cls=DjangoJSONEncoder)
        raw_data = serializers.serialize("python", context[self.context_object_name])
        context[self.context_object_name] = json.dumps([d['fields'] for d in raw_data])
        return context


class CourseListView(JSMixin, ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
