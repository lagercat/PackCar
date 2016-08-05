from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import DriverForm
from .models import Driver


@login_required
def submit_driver(request):
    form = DriverForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')
    return render(request, "drivers/create-route.html", {
        'form': form})


@login_required
def list_drivers(request):
    drivers = Driver.objects.order_by("-id").all()
    return render(request, "list.html", {
        "type": "Drivers",
        "drivers": drivers
    })


@login_required
def driver(request, slug):
    drivers = get_object_or_404(Driver, slug=slug)
    return render(request, "drivers/post.html", {
        "package": drivers
    })
