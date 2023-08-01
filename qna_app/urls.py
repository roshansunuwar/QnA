from django.urls import path

from . import views


urlpatterns = [
    path('', views.QuestionList.as_view(), name = 'home'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('contact/', views.ContactView.as_view(), name = 'contact'),
    path('<int:question_id>/', views.AnswerDetail.as_view(), name = 'answers'),
    path('facebook/', views.facebook_view, name='facebook'),
    path('instagram/', views.instagram_view, name='instagram'),
    path('twitter/', views.twitter_view, name='twitter'),
    path('youtube/', views.youtube_view, name='youtube'),
]