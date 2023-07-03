from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
class QuestionList(ListView):
    model = Questions
    template_name='qna_app/home.html'
    context_object_name = 'questions'
class AnswerDetail(DetailView):
    model = Questions
    template_name='qna_app/answer.html'
    context_object_name = 'questions'
    pk_url_kwarg = 'question_id'
