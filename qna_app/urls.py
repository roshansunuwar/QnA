from django.urls import path

from . import views


urlpatterns = [
    path('', views.QuestionList.as_view(), name = 'home'),
    path('<int:question_id>/', views.AnswerDetail.as_view(), name = 'answers'),
]