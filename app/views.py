from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from app.serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from app.models import Contact

# Create your views here.

def index (request):
    readdata=Contact.objects.all()
    return render(request,"index.html",{'x':readdata})

@api_view(['GET'])
def getdata(request):
    items=User.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deldata(request,id):
    try:
        item = get_object_or_404(User, pk=id)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)    

@api_view(['POST'])
def insdata(request):
    try:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            bg = serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response (status=status.HTTP_404_NOT_FOUND)             


        #_____api data update_______

@api_view(['POST'])
def updata(request,id):
    item = User.objects.get(pk=id)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    











    # ----------crud---form----------


def contact(request):
    username=request.POST["username"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    subject=request.POST["subject"]
    message=request.POST["message"]
    datasave=Contact(username=username,email=email,phone=phone,subject=subject,message=message)
    datasave.save()
    return redirect('home')  

def deletedata(request,id):
    member = Contact.objects.get(id=id) 
    member.delete()
    return redirect('home') 

def update(request,id):
    member = Contact.objects.get(id=id) 
    return render(request,"update.html",{'x':member})


def updatedata(request,id):
    member = Contact.objects.get(id=id)
    username=request.POST["username"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    subject=request.POST["subject"]
    message=request.POST["message"]
    member.username=username
    member.email=email
    member.phone=phone
    member.subject=subject
    member.message=message
    member.save()
    return redirect('home')


    

