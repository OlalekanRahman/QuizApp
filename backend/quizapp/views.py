from django.shortcuts import render
from rest_framework import serializers,generics
from rest_framework.views import APIView
from .serializers import QuizSerializer,RandomQuestionSerializer,QuestionSerializer
from .models import Quizzes,Questions
from rest_framework.response import Response
# Create your views here.
class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
