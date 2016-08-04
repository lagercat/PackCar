from django.shortcuts import render

from .forms import PackageForm


def submit_driver(request):
    form = PackageForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
    return render(request, "template_here", {
        'form': form})
