from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# HttpResponse is used to render html (not the best way beacuse we have hard coded html in the view)

def hello(request):
   text = """<h1>welcome to first application </h1>"""
   return HttpResponse(text)

'''
from django.shortcuts import render

def hello(request):
   return render(request, "API/template/hello.html", {})
'''


# We have used MVT format instead of hard coded html
# we have rendered hello.html directly to web page

