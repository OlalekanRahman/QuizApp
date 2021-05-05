from rest_framework import generics,serializers
from .models import Quizzes,Questions,Answers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields =['title','category']
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answers
        fields=['id','answer_text','correct_answer']

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True,many=True)

    class Meta:
        model = Questions
        fields = ['title','answer']

class QuestionSerializer(RandomQuestionSerializer):
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model=Questions
        fields = ['quiz','title','answer']
