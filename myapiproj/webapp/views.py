from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import coreapi 

# Create your views here.

def test(request):
    
    auth = coreapi.auth.BasicAuthentication(
    username='8762105645',
    password=''
    )
    client = coreapi.Client(auth=auth)
    schema = client.get('https://api.github.com/users?since=1000000')
    
    return HttpResponse(schema)#