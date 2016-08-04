
from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        template = 'homepages/home.html'
    else:
        template = 'homepages/index.html'
    return render_to_response(template,{
            'user': request.user,
            })
