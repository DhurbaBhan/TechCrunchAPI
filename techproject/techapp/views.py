from django.shortcuts import render,HttpResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
# Create your views here.
@api_view(['GET','POST'])
def tech(request):    
    if request.method == 'GET':
        prod=Post.objects.all()
        # result_list = list(prod)
        # return JsonResponse(json.dumps(result_list),safe=False)
        serial=PostSerializer(prod,many=True)
        return JsonResponse(serial.data,safe=False)

@api_view(['POST'])     
def tech_post(request):
    if request.method == 'POST':
        try:
            author=Author.objects.get(email=request.session['author_session_email'])
            if author.is_staff and request.session.has_key('author_session_email'):
                data = request.data
                serializer = PostSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()   
                    return JsonResponse({'msg':'Posted'})
            else:
                return Response("Either you are not approved by admin or you are not loggedin.")    
        except:        
            return Response("Either you are not approved by admin or you are not loggedin.")           
@api_view(['POST'])       
def client_login(request):
    if request.method=='POST':
        try:
            user=Client.objects.get(email=request.data.get('email'))
            if request.data.get('password')==user.password:
                # storing session with session key 'session_email'
                request.session['session_email']=user.email
                return Response("logged in successfully.")
            else:
                return Response("Invalid email or password!!") 

        except:
            return Response("Invalidd email or password!!")
@api_view(['GET'])       
def client_logout(request):
    if request.method=='GET':
        if request.session.has_key('session_email'):
            # destroying the session in order to logout user from the system
            del request.session['session_email']  
            return Response("loggedout successfully!!!") 

@api_view(['POST'])       
def author_login(request):
    if request.method=='POST':
        try:
            user=Author.objects.get(email=request.data.get('email'))
            if request.data.get('password')==user.password:
                # storing session with session key 'session_email'
                request.session['author_session_email']=user.email
                return Response("Author logged in successfully.")
            else:
                return Response("Invalid email or password!!") 

        except:
            return Response("Invalidd email or password!!")
@api_view(['GET'])       
def author_logout(request):
    if request.method=='GET':
        
        if request.session.has_key('author_session_email'):
            # destroying the session in order to logout user from the system
            del request.session['author_session_email']  
            return Response("Author loggedout successfully!!!")          

@api_view(['POST']) 
def comment(request):
    if request.method=='POST':
        if request.session.has_key('session_email'):
            data=request.data
            print(data)
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()   
                return Response('Comment Posted')
        else:
            return Response("Client, Login First to comment!!!")     
    

    
