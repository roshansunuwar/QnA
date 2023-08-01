from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, TemplateView

from .models import *

# Create your views here.
class QuestionList(ListView):
    model = Questions
    template_name='qna_app/home.html'
    context_object_name = 'questions'

class AboutView(TemplateView):
    template_name='qna_app/about.html'
class ContactView(TemplateView):
    template_name='qna_app/contact.html'
class AnswerDetail(DetailView):
    model = Questions
    template_name='qna_app/answer.html'
    context_object_name = 'questions'
    pk_url_kwarg = 'question_id'

def facebook_view(request):
    return redirect('https://www.facebook.com')

def twitter_view(request):
    return redirect('https://www.twitter.com')

def instagram_view(request):
    return redirect('https://www.instagram.com')

def youtube_view(request):
    return redirect('https://www.youtube.com')