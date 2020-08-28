from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
import json


from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
#create ... views

def magazineUS(request):
    return  render( request , 'magazine/magazineUS.html',{})

def magazineMain(request):
    return render(request, 'magazine/magazineMain.html', {})

def post_list(request) :
    return  render( request , 'blog/post_list.html',{})

@csrf_exempt
def sendValue(request):
    test = {'test11': 'mytest' }       
    return render( request , 'blog/post_list.html',{'test': test})
    '''
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    }, json_dumps_params = {'ensure_ascii': True})
    '''