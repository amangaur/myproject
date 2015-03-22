from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import datetime
from polls.models import Question,Choice
# Create your views here.
def hello(request):
    return HttpResponse("hello world")

def questions(request):
    data=serializers.serialize('json',Question.objects.all())
    return HttpResponse(data,content_type="application/json")

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>it is now%s.</body></html>"%now
    return HttpResponse(html)
    
def choices(request,question_id):
    question_id=int(question_id);
    choices=Choice.objects.filter(question=Question.objects.filter(id=question_id))
    data=serializers.serialize('json',choices)
    return HttpResponse(data,content_type="application/json")
