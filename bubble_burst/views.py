from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from bubble_burst.models import User

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_user(request, user_name):
    if request.method == 'GET':
        try:
            user = User.objects.get(name=user_name)
            response = json.dumps([{ 'User': user.name, 'Score': user.score}])
        except:
            response = json.dumps([{ 'Error': 'User name not found' }])
    return HttpResponse(response, content_type='text/json')

def get_users(request):
    if request.method == 'GET':
        try:
            users = []
            for user in User.objects.all().values():
                users.append(user)
            response = json.dumps(users)
        except:
            response = json.dumps([{ 'Error': 'Error' }])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        user_name = payload['name']
        score = payload['score']
        user = User(name=user_name, score=score)
        try:
            user.save()
            response = json.dumps([{ 'Success': 'User added successfully' }])
        except:
            response = json.dumps([{ 'Error': 'User not added' }])
    return HttpResponse(response, content_type='text/json')
