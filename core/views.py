from django.shortcuts import render, redirect
from .forms import UserCreationForm, VerifyForm
from django.contrib.auth.decorators import login_required
from .decorators import verification_required
from . import verify


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("phone ---> ", form.cleaned_data.get('phone'))
            verify.send(form.cleaned_data.get('phone'))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/authentication/register.html', {'form': form})


@login_required
@verification_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('index')
    else:
        form = VerifyForm()
    return render(request, 'core/verify.html', {'form': form})
