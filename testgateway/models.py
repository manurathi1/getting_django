from django.db import models

# Create your models here.

class Questions(models.Model):
    description = models.TextField()
    answerA = models.TextField()
    answerB = models.TextField()
    answerC = models.TextField()
    answerD = models.TextField()
    correctAnswer = models.TextField()
    image = models.BooleanField()

    def get_question(self, pk):
        return self.objects.get(pk = pk)



