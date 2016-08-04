from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


# Create your views here.

@login_required
def login_page(request):
    errors = []
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                errors.append('Incorrect username or password')

        else:
            errors.append('Invalid form')
    return render(request, "authentication/logIn.html", {
        'form': form,
        'errors': errors})
