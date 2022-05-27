from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home_view(request):    
    return render(request, "user_example/home.html")

@login_required
def special(request):    
    return render(request, "user_example/special.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username= username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)