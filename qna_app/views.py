from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import *

# Create your views here.
def home(request):
    questions = Questions.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'qna_app/home.html', context)

def answer(request, question_id):
     #!shortcut
    questions = get_object_or_404(Questions, pk = question_id)
    context = {
        'questions' : questions,
    }


    return render(request, 'qna_app/answer.html', context)