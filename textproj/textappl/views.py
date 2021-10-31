from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def homePageView(request):
    return render(request, "index.html")
def editview(request):
    return render(request, "EditHome.html")
def signup(request):
    if request.method=="POST":
        name = request.POST.get('name')
        addr=request.POST.get('address')
        email = request.POST.get('email')
        uname=request.POST.get('username')
        pas=request.POST.get('password')

        l=login()

        l.username=uname
        l.password=pas
        l.role=1
        l.save()

        r=registration()

        r.name=name
        r.email=email
        r.address=addr
        r.username = uname
        r.password = pas
        r.logid=l
        r.save()
        return render(request,"index.html")
    else:
        return render(request,"register.html")
def insertTag(request):
    if request.method=="POST":
        tagname = request.POST.get('tag')
        text = request.POST.get('text')

        username=request.session.get('username')
        tagobjfo = tagtbl.objects.filter(tag=tagname)

        ##tagtbl tagId;

        if(tagobjfo.exists()):
            tagId = tagtbl.objects.get(tag=tagname)
        else:
            tagobj = tagtbl()
            tagobj.tag = tagname
            tagobj.save()
            tagId = tagtbl.objects.get(tag=tagname)

        print("tagId------------------",tagId.tag,text)
        snipObj=textsnippettbl()

        snipObj.text= text
        snipObj.user=username

        snipObj.tagid=tagId
        snipObj.save()
        textlist = textsnippettbl.objects.all()
        return render(request, "display.html", {"textlist": textlist})
    else:
        return render(request,"register.html")

def update(request,textid):

    print("test")
    d = textsnippettbl.objects.get(id=textid)
    print("after")

    if request.method == "POST":
        text = request.POST.get('text')
        username=request.session.get('username')
        tag = request.POST.get('tag')
        tagobjfo = tagtbl.objects.filter(tag=tag)

        ##tagtbl tagId;

        if (tagobjfo.exists()):
            tagId = tagtbl.objects.get(tag=tag)
        else:
            tagobj = tagtbl()
            tagobj.tag = tag
            tagobj.save()
            tagId = tagtbl.objects.get(tag=tag)

        d.text = text
        d.user = username
        d.tagId = tagId

        d.save()
        textlist = textsnippettbl.objects.all()
        return render(request, "display.html", {"textlist": textlist})
    else:
        return render(request, "EditHome.html", {"textobj": d})

def signin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pas = request.POST.get('password')
        if (login.objects.filter(username=uname,password=pas).exists()):
            log=login.objects.filter(username=uname,password=pas)
            for i in log:
                lid=i.id
                r=i.role
                if r==1:
                    request.session['userid']=lid
                    request.session['username'] = uname
                    reg=registration.objects.get(logid_id=lid)
                    textlist=textsnippettbl.objects.all()
                    return render(request,"userHome.html",{"textlist":textlist})
                else:
                    return HttpResponse("admin login")
        else:
            return HttpResponse("No user")
    else:
        return render(request, "login.html")

