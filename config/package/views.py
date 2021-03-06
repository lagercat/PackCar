import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden

from .forms import PackageForm,EditPackageForm
from .models import Package, Offer


@login_required
def submit_package(request):
    form = PackageForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/alldrivers')
    print form.errors
    return render(request, "package/create_package.html", {
        'form': form,
        'user': request.user})


@login_required
def list_packages(request):
    packages = Package.objects.order_by("-id").all()
    return render(request, "list.html", {
        "type": "Packages",
        "packages": packages})
    

@login_required
def package(request, slug):
    package = get_object_or_404(Package, slug=slug)
    if request.method == 'POST':
        if request.POST.get("deletePost") and package.author == request.user:
            package.delete()
            return redirect('/')
    return render(request, "package/post.html", {
        "package": package
    })


@login_required
def manager(request):
    if request.method == 'POST':
        print "dd"
    return render(request, "package/manager.html", {

    })


@login_required
@csrf_exempt
def accept(request, slug):
    offer = get_object_or_404(Offer, id=slug)
    if offer.driver_user != request.user:
        return HttpResponseForbidden()
    offer.accepted = True
    offer.save()
    return redirect('/manager')

@login_required
@csrf_exempt
def decline(request, slug):
    offer = get_object_or_404(Offer, id=slug)
    if offer.driver_user != request.user:
        return HttpResponseForbidden()
    offer.delete()
    return redirect('/manager')


@login_required
@csrf_exempt
def finish(request, slug):
    offer = get_object_or_404(Offer, id=slug)
    if offer.driver_user != request.user:
        return HttpResponseForbidden()
    offer.completed = True
    offer.save()
    return redirect('/manager')


@login_required
def edit_package(request, slug):
    post = get_object_or_404(Package, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = EditPackageForm(request.POST or None, request.FILES or None,
                        instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/package/' + post.slug)
    return render(request, 'package/edit_package.html', {
        'post': post,
        'form': form,
    })
