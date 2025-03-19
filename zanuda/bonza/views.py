from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reguest):
    return HttpResponse('<h2>Это моя первая страница на Django</h2>')

def data(reguest):
    return HttpResponse('<h2>Это моя вторая страница data на Django</h2>')


def test(reguest):
    return HttpResponse('<h2>Это моя третья страница test на Django</h2>')