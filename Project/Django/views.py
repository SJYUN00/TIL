from django.shortcuts import render
from django.http import HttpResponse
 
from .models import Candidate
 
# Create your views here.
def index(request):
    info_stock = Candidate.objects.all()
    context = {'info_stock':info_stock}
        #context에 모든 주식 정보를 저장
    return render(request, 'elections/index.html', context)
        #context안에 있는 주식 정보를 index.html로 전달