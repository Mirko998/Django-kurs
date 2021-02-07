from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'cms/index.html', {'test':'Ulogovan'})
    else:
        return render(request, 'cms/index.html', {'test':'Nije ulogovan'})
