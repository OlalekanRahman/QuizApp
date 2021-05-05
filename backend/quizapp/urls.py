from django.urls import path
from .views import QuizView,RandomQuestion,QuizQuestion

urlpatterns = [
    path('', QuizView.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random_question'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions')
    ]
