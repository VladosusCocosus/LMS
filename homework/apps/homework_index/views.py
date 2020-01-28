from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
import json, requests, time
from bs4 import BeautifulSoup
import datetime
import update_temp



def homework_list(request):
    weather_yandex = update_temp.yandex_pogoda()
    act_data = update_temp.get_act_data()
    print(act_data)
    #response = requests.get("https://sitv.ru/actirovka/")
    #act = str(BeautifulSoup(response.text, features="lxml").find_all('p')[0])[3:63]
    #act = act.split('<')

    last_homework = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'homework/homework.html', {'homework':last_homework, 'temper_now':weather_yandex, 'check': 0, 'act':act_data })

@login_required(login_url='/accounts/login/')
def homework_create_page(request):
    return render(request ,'homework/homework_create.html')

@login_required(login_url='/accounts/login/')
def homework_create_page_success(request):
    date = request.POST['date'].split('-')
    cor_date = date[0] + date[1] + date[2]
    new_articles = Article.objects.create(homework_author = request.user.first_name, homework_lesson = request.POST['article_title'], homework = request.POST['article_text'], date_for_server = str(cor_date), use_date = request.POST['date'], pub_date = timezone.now())
    return HttpResponseRedirect(redirect_to='../../../')

def search(request):
    data_all = request.POST['data_search']
    date = request.POST['data_search'].split('-')
    date_url = date[0] + date[1] + date[2]
    return HttpResponseRedirect(reverse('homework:resalt', args=[date_url],))

def resalt(request, date_url):
    homework = Article.objects.filter(date_for_server=date_url)
    return render(request, 'homework/correct_homework.html', {'homework':homework})

def tomorrow(request):
    today = datetime.datetime.now()
    month = str(today.month)
    if len(month) == 1:
        month = str(0) + month
    else:
        pass
    day = today.day + 1
    date_url = str(today.year) + month + str(day)
    return HttpResponseRedirect(reverse('homework:resalt', args=[date_url],))
