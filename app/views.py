from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.

def index(request):
    return HttpResponse('request')


def profile(request):
    jsonDataList = []
    selectData = {}
    newDataList = []

    req = requests.get('http://api.github.com/users/yimikao')
    parsedJson =  json.loads(req.content)

    jsonDataList.append(parsedJson)

    for data in jsonDataList:
        selectData['name'] = data['name']
        selectData['blog'] = data['blog']
        selectData['email'] = data['email']
        selectData['public_gists'] = data['public_gists']
        selectData['public_repos'] = data['public_repos']
        selectData['avatar_url'] = data['avatar_url'] 
        selectData['followers'] = data['followers'] 
        selectData['following'] = data['following'] 

    newDataList.append(selectData) 

    return HttpResponse(newDataList)
    


