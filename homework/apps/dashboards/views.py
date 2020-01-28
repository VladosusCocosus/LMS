from django.shortcuts import render

from django.utils import timezone
import datetime

def dashboards(request):
    dt = datetime.datetime.now()
    week = dt.isocalendar()[1]
    if week % 2 == 0:
        return render(request, 'dashboard/dashboard.html', {'week': True})
    else:
        return render(request, 'dashboard/dashboard.html', {'week': False})