from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse



def reg(request):
    username = request.user.username
    return render(request, 'registration/reg_panel.html', {'user':username})


def reg_succes(request):
    user = User.objects.create_user(username= request.POST['username'], first_name= request.POST['first_name'], email= request.POST['email'], last_name= request.POST['last_name'], password= request.POST['password'])
    user.last_name = request.POST['last_name']
    user = form.save(commit=False)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('registration'))