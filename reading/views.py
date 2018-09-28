from django.shortcuts import render,redirect,reverse

# Create your views here.
def reading_view1(request,name,**kwargs):
    print(name)
    print(kwargs)
    return  redirect(reverse('one',args=(name,)))
    # return render(request,'reading/reading.html')
