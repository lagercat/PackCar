from django.shortcuts import render

from .forms import PackageForm
from .models import Package


def submit_package(request):
    form = PackageForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
    return render(request, "template_here", {
        'form': form})


def list_packages(request):
    packages = Package.objects.order_by("-id").all()
    return render(request, "list.html", {
        "type": "Packages",
        "packages": packages})
