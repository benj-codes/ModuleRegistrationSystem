from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
#from course.models import Course
from modules.models import Module
from django.views.generic import DetailView
from django.contrib.auth.models import Group

# Create your views here.

@login_required
def modules(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH: ', search_query)
        modules = Module.objects.filter(name__icontains=search_query, courses__name = request.user.groups.first().name)
    else:
        modules = Module.objects.filter(courses__name = request.user.groups.first().name)

    for module in modules:
        print(module.name, module.courses.all())

    modules_list = {'modules': modules, 'title': 'Available Modules'}

    return render(request, 'modules/modules.html', modules_list)

# """ def get_modules_for_course(student_course):
#     return Module.objects.filter(course=student_course) """

class ModuleDetailView(DetailView):
    model = Module

    def my_view(request, code):
        module = Module.objects.get(pk=code)
        return render(request, 'modules/modules.html', {'module': module})

