from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, "fscohort/home.html")

class HomeView(TemplateView):
    template_name = "fscohort/home.html"


def student_list(request):
    students = Student.objects.all()
    context = {
        "students":students
    }
    return render(request, "fscohort/student_list.html", context)

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
       "form":form
    }
    return render(request, "fscohort/student_add.html", context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_add.html'
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        self.object = form.save()
        if not self.object.number:
            self.object.number = 9999
        self.object.save()
        return super().form_valid(form) 
    










def student_detail(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }
    return render(request, "fscohort/student_detail.html", context)

class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context= {
        "student":student,
        "form":form
    }
    return render(request, "fscohort/student_update.html", context)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html"
    success_url = reverse_lazy('list')
    # pk_url_kwarg = 'id'







def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "fscohort/student_delete.html"
    success_url = reverse_lazy('list')
    # pk_url_kwarg = 'id'