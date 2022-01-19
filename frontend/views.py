from django.shortcuts import render
from django.db import connection
from frontend.models import displaydata

# Create your views here.

def list(request):
    return render(request, 'frontend/list.html')

def tablesjoin(request):
    cursor=connection.cursor()
    cursor.execute("select country.Cid,country.Cname,state.Sname from country join state on country.Cid=state.Cid")
    results=cursor.fetchall()
    return render(request, 'table.html',{'displaydata':results})