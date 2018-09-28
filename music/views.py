from django.shortcuts import render

# Create your views here.
def music_view1(request,name):
    return render(request,'music.html',{'name':name})