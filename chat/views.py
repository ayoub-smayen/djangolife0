from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from stream_chat import StreamChat

from .models import Member

@csrf_exempt
def init(request):
    if not request.body:
        return JsonResponse(status=200, data={'message': 'No request body'})
    body = json.loads(bytes(request.body).decode('utf-8'))
    # or ('pic_profle' not in body) or('description' not in body):
    if 'username' not in body  :
        return JsonResponse(status=400, data={'message': 'Username is required to join the channel'})

    username = body['username']
    #pic_profle = body['pic_profle']
    #description =body['description']


    client = StreamChat(api_key=settings.STREAM_API_KEY,
                        api_secret=settings.STREAM_API_SECRET)
    channel = client.channel('messaging', 'General')

    try:
        member = Member.objects.get(username=username)
        token =str(bytes(client.create_token(
            user_id=username),encoding="utf-8").decode('utf-8'))
        return JsonResponse(status=200, data={"username": member.username, "token": token, "apiKey": settings.STREAM_API_KEY})

    except Member.DoesNotExist:
        member = Member(username=username)
        member.save()
        token =str(bytes(client.create_token(
            user_id=username),encoding="utf-8").decode('utf-8'))
        client.update_user({"id": username, "role": "admin"})
        channel.add_members([username])
        # "description":member.description,"pic_profle":pic_profle,,description=description, pic_profle=pic_profle
        return JsonResponse(status=200, data={"username": member.username, "token": token, "apiKey": settings.STREAM_API_KEY})
        #"description":member.description,"pic_profle":pic_profle,
