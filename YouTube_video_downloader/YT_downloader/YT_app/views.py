from django.shortcuts import render
from django.http import *
from pytube import YouTube

def index(request):
    try :
        if request.POST.get('search'):
            url = request.POST.get('url')
            video = YouTube(url)
            vid_title = video.title
            vid_prevju = video.thumbnail_url
            quality, streams = [], []
            for qu in video.streams.filter(progressive=True):
                quality.append(qu.resolution)
                streams.append(qu)
            return render(request, 'index.html', {'vid_title': vid_title, 'vid_prevju': vid_prevju, 'quality': quality, 'streams': streams, 'url': url})

        elif request.POST.get('download'):
            url = request.POST.get('url')
            video = YouTube(url)
            stream = [x for x in video.streams.filter(progressive=True)]
            quality = video.streams[int(request.POST.get('download')) -1]
            quality.download() 
            return render(request, 'index.html', {'status': 'Your video has been downloaded'})
    except :
        return render(request, 'index.html', {'status': "Incorrect URL address, try agan"})
    return render(request, 'index.html')