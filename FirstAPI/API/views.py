from django.shortcuts import render
# Create your views here.

import json

from django.http import HttpResponse

# HttpResponse is used to render html (not the best way beacuse we have hard coded html in the view)

def hello(request):
   msg = """Hi, U r inside ur first application """
   return HttpResponse(msg)


'''
from django.shortcuts import render
def hello(request):
   return render(request, "FirstAPI/FirstAPI/API/hello.html", {})
'''

# We have used MVT format instead of hard coded html
# we have rendered hello.html directly to web page
