from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .forms import DriverForm, EditDriverForm
from .models import Driver


@login_required
def submit_driver(request):
    form = DriverForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/driver/' + str(form.instance.slug))
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
    if request.method == 'POST':
        if request.POST.get("deletePost") and drivers.author == request.user:
            drivers.delete()
            return redirect('/')
    return render(request, "drivers/post.html", {
        "package": drivers,
        "user": request.user
    })


@login_required
def edit_drivers(request, slug):
    post = get_object_or_404(Driver, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditDriverForm(request.POST or None, request.FILES or None,
                          instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/driver/' + post.slug)
    return render(request, 'drivers/edit_rout.html', {
        'post': post,
        'form': form,
    })
