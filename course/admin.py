from django.contrib import admin

from course.models import Course, Chapter, Section, Fragment

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Section)
admin.site.register(Fragment)
