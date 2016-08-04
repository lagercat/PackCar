from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from .forms import LoginForm, UserRegisterForm


# Create your views here.

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
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


def register_page(request):
    form = UserRegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    return render(request, "authentication/register.html", {
        'form': form,
    })
