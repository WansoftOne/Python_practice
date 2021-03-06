"""Post Views"""

#Django
from django.shortcuts import render
#Utilities
from datetime import datetime

posts = [
    {
        'title':'Mont Blac',
        'user':{
            'name':'Yesica Cortes',
            'picture':'https:picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https:picsum.photos/800/600/?image=1036',
    },
    {
        'title':'Via Lactea',
        'user':{
            'name':'Christian Van der Henst',
            'picture':'https:picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https:picsum.photos/800/600/?image=903',
    },
    {
        'title':'Nuevo auditorio',
        'user':{
            'name':'Uriel (thespianartist)',
            'picture':'https:picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https:picsum.photos/800/600/?image=1076',
    },
]

def list_post(request):
    return render(request, 'feed.html', {'posts':posts})
