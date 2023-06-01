from django.db import models

# Create your models here.
class Questions(models.Model):
    question_title = models.CharField(max_length=200)
    question_text = models.TextField()

    def __str__(self):
        return self.question_title


class Answers(models.Model):
    question_title = models.ForeignKey(Questions, on_delete=models.CASCADE)
    solution = models.TextField()

    
    # def __str__(self):
    #     return self.question_title