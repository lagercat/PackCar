from django.shortcuts import render

from .forms import DriverForm


def submit_driver(request):
    form = DriverForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance = request.user
            form.save()
    return render(request, "template_here", {
        'form': form})
