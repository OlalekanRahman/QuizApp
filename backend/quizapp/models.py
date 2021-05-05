from django.db import models
#from django.validators import RegexValidator

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural='Categories'
    name = models.CharField(max_length=10, blank =False)
    def __str__(self):
        return self.name

class Quizzes(models.Model):
    class Meta:
        verbose_name='Quiz'
        verbose_name_plural='Quizzes'
        ordering =['id']
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20, default='new Quiz', verbose_name='New Quizzes')
    date_created= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class updated(models.Model):
    class Meta:
        abstract=True
    date_updated=models.DateTimeField( auto_now=True, verbose_name='last updated')

class Questions(updated):
    class Meta:
        verbose_name='Question'
        verbose_name_plural='Questions'
        ordering =['id']
    difficulty = (('0','simple'),('1','moderate'),('2','hard'))
    type=((0,'Multiple_choice'),(1,'Cloze_Test'))
    title=models.CharField(max_length=100,verbose_name='Title')
    quiz = models.ForeignKey(Quizzes, related_name='question',on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True, verbose_name='active mode')
    tecnhique = models.IntegerField(choices=type,default=0,verbose_name='Type of Question')
    difficulty = models.IntegerField(choices = difficulty,default=0,verbose_name='Difficulty')
    date_created=models.DateTimeField(auto_now_add=True,verbose_name='Date created')

    def __str__(self):
        return self.title


class Answers(updated):
    class Meta:
        verbose_name='Answer'
        verbose_name_plural='Answers'
        ordering =['id']
    question =models.ForeignKey(Questions,related_name='answer',on_delete=models.DO_NOTHING)
    correct_answer = models.BooleanField(default=False, verbose_name='Correct Answer')
    answer_text= models.TextField(max_length=600,verbose_name='Answer Text')
    def __str__(self):
        return f'{self.question} :Answer => {self.answer_text}'
