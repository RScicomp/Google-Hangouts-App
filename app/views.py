from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView

from .models import Greeting
from .models import Summaryform
from .models import Schedulingform
from .models import UploadFileForm
from .models import FileFieldForm
from .models import Hangoutsform
from .models import *
from .firebaseimp import firebase
from django.shortcuts import redirect


from .scheduler import schedule, advisor, startup
from .AnalyzeEvents import compare,similar,getallreviews,getallreviews18,getallreviews19,getallreviewsdd
import pandas as pd
import openpyxl
# Create your views here.
 

def index(request):
    
    if request.method=='POST':
        form = Summaryform(request.POST)
        sform = Schedulingform(request.POST)
        # Summarizer
        if form.is_valid():
            print(len(form.cleaned_data['data'].split()))
            summary = build_summary(form.cleaned_data['data'],.5) 
            print(summary)
            form = Summaryform()
            sform = Schedulingform
            return render(request,'index.html',{'Summary':summary,'form':form,'schedulingform':sform})
        # Scheduler
        if sform.is_valid():
            advisorno = sform.cleaned_data['advisorno']
            startupno = sform.cleaned_data['startupno']
            timeslotno = sform.cleaned_data['timeslotno']
            groupsize = sform.cleaned_data['groupsize']
            s = schedule(advisorno,startupno,timeslotno,groupsize)
            try:
                s = s.dbuildschdule(advisor,startup,pd)
                results = s
                s = s.to_html()
                sform = Schedulingform()
                form = Summaryform()
                
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=filename.csv'

                results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=".")
            except:
                return render(request, 'index.html',{'form':form,'Schedule':s, 'schedulingform':sform})

            return response
            #return render(request, 'index.html',{'form':form,'Schedule':s, 'schedulingform':sform})
    
    else:
        form = Summaryform()
        sform = Schedulingform()
        print("Default")
        return render(request,'index.html',{'form':form,'schedulingform':sform})

#decprecated
def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_uploaded_file2(f,sheetname='Sheet1'):
    wb = openpyxl.load_workbook(f)
    # getting a particular sheet by name out of many sheets
    worksheet = wb[sheetname]
    print(worksheet)
    excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    df = pd.DataFrame(excel_data)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    return(df)

def outputevents(file):
    output19 = handle_uploaded_file2(file,sheetname='2019 Selection Day')
    output18 = handle_uploaded_file2(file,sheetname='2018 Selection Day')
    dd19 = handle_uploaded_file2(file,sheetname='DD 19')
    advisors = handle_uploaded_file2(file,sheetname='Advisors')

    output19['What is your e-mail?']=output19['What is your e-mail?'].str.lower()
    output18['What is your e-mail?']=output18['What is your e-mail?'].str.lower()
    dd19['What is your e-mail?']=dd19['What is your e-mail?'].str.lower()
    s = advisors['Email'].str.lower()
    advisors['Email']=s
    correct = s

    print(output19['What is your e-mail?'])

    #Get correct Emails
    #output19['What is your e-mail?']=compare(correct,list(output19['What is your e-mail?']))
    #output18['What is your e-mail?']=compare(correct,list(output18['What is your e-mail?']))
    #dd19['What is your e-mail?']=compare(correct,list(dd19['What is your e-mail?']))

    sel19 = getallreviews19(output19)
    sel18 = getallreviews18(output18)
    dd19 = getallreviewsdd(dd19)
    r = pd.merge(sel18,sel19,on='Email',how='outer')
    r=pd.merge(dd19,r,on='Email',how='outer')
    print(r)
    return(r)

def leaderboard2(request):
    if request.method == 'POST':
        print("POST")
        fileform = UploadFileForm(request.POST, request.FILES)
    
        if fileform.is_valid():
            print("VALID")
            results = handle_uploaded_file2((request.FILES['file']))
    else:
        fileform = UploadFileForm()

    return render(request, 'leaderboard.html', {'fileform': fileform,'filefields':filefields})

def leaderboard(request):
    if request.method == 'POST':
        print("POST")
        fileform1 = UploadFileForm(request.POST, request.FILES)
  
        if fileform1.is_valid():
            print("ALL VALID")
            results=outputevents(request.FILES['file'])
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            results.to_csv(path_or_buf=response,sep=',',float_format='%.2f',index=False,decimal=",")
            return(response)
    else:
        fileform1 = UploadFileForm()

    return render(request, 'leaderboard.html', {'fileform': fileform1})

def words(request):

    if (request.method=='POST'):
        print("POST")
        form = Summaryform(request.POST) 
        if form.is_valid():
           l = len(form.cleaned_data['data'])
           print(l)
           return render(request,'wordcounter.html',{'Length':l,'form':form})
    else:
        form = Summaryform()
    return render(request,'wordcounter.html',{'form':form})

def hangouts(request):
    db=firebase.database()
    alllinks=[]
    allnames=[]
    form = Hangoutsform()
    enterform= Roomform()
    if (request.method=='POST'):

        print("POST")
        form = Hangoutsform(request.POST) 
        alllinks=[]
        if enterform.is_valid():
            return(request)
        if form.is_valid():
           l = form.cleaned_data['link']
           name = form.cleaned_data['name']
           password = form.cleaned_data['password']
           data = {"link": l,"name":name,"no":0,"password": password}
           if("hangouts.google.com/call" in data['link']):
             db.child("links").push(data)
           links = db.child("links").get()
           vals=list(dict(links.val()).values())
           for link in vals:
                room=Roomform()
                room.toenter=link['password']
                room.roomurl = link['link']
                alllinks.append((link['link'],link['name'],link['no'],room))
           return render(request,'hangouts.html',{'Name':name,'Link':l,'form':form,'Data':alllinks})
          
    else:
        links = db.child("links").get()
        vals=list(dict(links.val()).values())
        for link in vals:
            room=Roomform()
            room.toenter=link['password']
            room.roomurl = link['link']
            alllinks.append((link['link'],link['name'],link['no'],room))
    
    #alllinks=[("WWW.GOOGLE.CA","HELLO")]
    return render(request,'hangouts.html',{'form':form,'Data':alllinks})

def movies(request):
    db=firebase.database()
    form = Movieform()
    if(request.method=='POST'):
        print('POST')
        form = Movieform(request.POST)
        if form.is_valid():
            movie_type = form.cleaned_data['movie_type']
            movie_name = form.cleaned_data['movie_name']
            data = {'movie_type':movie_name, 'movie_name': movie_name}


def db(request):
    
    greeting = Greeting()

    #greeting.save()

    #greetings = Greeting.objects.all()
    #print("We here")
    return render(request, "db.html", {"greetings": greetings})
