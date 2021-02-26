from django.shortcuts import render
from pytube import YouTube
from  django.http import HttpResponse


# Create your views here.
def sho(request):
    return render(request,'index.html')
def next(request):
    n1=request.GET['text1']
    yt=YouTube(n1)
    thumb=yt.thumbnail_url
    name=yt.title
    r=yt.streams
    reso=yt.streams.order_by('resolution')
    l=n1

    d={'thumbnail':thumb,'name':name,'link':l}
    return render(request,'index.html',d)
def download(request):
    link=request.GET['lj']

    format=request.GET['quality']
    yt = YouTube(link)
    Save_Path = "H:/"
    if format=='audio':
        yt.streams.filter(only_audio=True).first().download()
    else:
        yt.streams.filter(res=format).first().download(Save_Path)
    return  HttpResponse('Downloaded')











