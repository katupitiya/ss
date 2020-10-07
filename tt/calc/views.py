from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

import pymongo
from pymongo import MongoClient


connection = MongoClient('localhost', 27017)
db = connection.text


def home(request):


    #db.text1.insert({"name": uname})
    return render(request, 'index.html');

def home2(request):
    uname = request.GET['name1']

    db.text1.insert({"name": uname})
    return render(request, 'index.html');