from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
#from course.models import Course
from modulesreg.models import Module
from django.views.generic import DetailView

# Create your views here.

@login_required
def modules(request):
    print(Module.objects.all())
    modules_list = {'modules': Module.objects.all(), 'title': 'Complete List of Modules'}
    return render(request, 'modulesreg/modules.html', modules_list)

# """ def get_modules_for_course(student_course):
#     return Module.objects.filter(course=student_course) """

class ModuleDetailView(DetailView):
    model = Module

    def my_view(request, code):
        module = Module.objects.get(pk=code)
        return render(request, 'modulesreg/modules.html', {'module': module})

