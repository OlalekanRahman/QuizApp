from django.contrib import admin

# Register your models here.
from .models import Category, Quizzes, Questions, Answers
#admin.site.register(Answers)
@admin.register(Category)

class CatAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display=['id','title']


class AnswerInlineModel(admin.StackedInline):
    model = Answers
    fields=['answer_text','correct_answer']



@admin.register(Questions)

class QuestionAdmin(admin.ModelAdmin):
    fields=['title','quiz']
    list_display=['title','quiz','date_updated']
    inlines = [AnswerInlineModel]
@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['answer_text','correct_answer','question']
