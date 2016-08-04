from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .forms import PackageForm
from .models import Package


@login_required
def submit_package(request):
    form = PackageForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')
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
    package = Package.get_object_or_404(Package, slug=slug)
    return render(request, "template.html", {
        "package": package
    })
