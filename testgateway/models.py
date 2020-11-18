from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

# Create your models here.

class Questions(models.Model):
    description = models.TextField()
    answerA = models.TextField()
    answerB = models.TextField()
    answerC = models.TextField()
    answerD = models.TextField()
    correctAnswer = models.TextField()
    image = models.BooleanField()
    test = models.ForeignKey('Tests', default= 1, on_delete = models.SET_DEFAULT)
    
    def get_question(self, pk):
        return self.objects.get(pk = pk)

    def __str__(self):

        return self.description[0:10]



class Tests(models.Model):

    # test_difficulty = models.
    slug = models.SlugField()

    def get_absolute_url(self):

        return reverse('test_landing', kwargs={'slug': self.slug})


# class Profile(models.Model):

#     user = models.OneToOneField(settings.AUTH_USER_MODEL,von_delete=models.CASCADE)
#     question = models.ManyToManyField('Questions', related_name = 'question')
#     time 


#user created 
#profile defuat created
# 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userStat = models.ManyToManyField('Questions', through='Userstats', blank=True)
    
    def __str__(self):
        return self.user.username

class Userstats(models.Model):
    userProfile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    questions = models.ForeignKey('Questions', on_delete=models.CASCADE)
    submitAnswer = models.CharField(max_length = 50, blank=True)
    time = models.DurationField(default= timedelta(seconds=0))

    def __str__(self):
        return self.userProfile.user.username


# class Usertestprofile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     questions = models.ManyToManyField('Questions', blank=True)
#     submitAnswer = models.CharField(max_length = 50, blank=True)


#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Usertestprofile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.usertestprofile.save()
#         tmpuser = Usertestprofile.objects.filter(user = instance).first()
#         for question in Questions.objects.all():
            
#             tmpuser.questions.add(question)
#             tmpuser.save()



