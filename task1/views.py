from django.http import HttpResponse

def view_one(request):
    return HttpResponse("我是第一个view.")