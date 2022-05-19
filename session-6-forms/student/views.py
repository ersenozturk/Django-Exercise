from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    # print(request.POST)
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        if 'profile_pic' in request.FILES:
            # student.profile_pic = request.FILES['profile_pic']
            student.profile_pic = request.FILES.get('profile_pic')
            student.save()
        messages.success(request,"Student saved successfully")
        messages.error(request,"testing failed message")
        return redirect('student')
        # print(form.cleaned_data.get('first_name'))

    context = {
        'form':form
    }

    return render(request,'student/student.html',context)
