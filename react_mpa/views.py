import os

from django.core import serializers
import json


class ReactViewMixin:
    def get_bundle_path(self):
        if self.template_name is None:
            # find a default template name using an ancestor other than this class and self's class
            for klass in self.__class__.__mro__:
                if klass != ReactViewMixin and klass != self.__class__ and hasattr(klass, "get_template_names"):
                    template_name = super(klass, self).get_template_names()[0]
                    break
        else:
            template_name = self.template_name

        # replace .html with .js
        return os.path.splitext(template_name)[0] + ".js"

    context_object_name = "react_props"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # serialize the generic context data
        raw_data = serializers.serialize("python", context[self.context_object_name])
        context[self.context_object_name] = json.dumps([d['fields'] for d in raw_data])

        return context

    def get_template_names(self):
        template_names = super().get_template_names()

        # if template name is defined in one of the non-generic ancestors, return.
        # refer to SingleObjectTemplateResponseMixin or MultipleObjectMixin for more info
        if len(template_names) > 1:
            return template_names
        else:
            # put react_base.html to the front
            return ["react_base.html"] + template_names
