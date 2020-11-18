from django.contrib import admin

# Register your models here.
from .models import Questions, Tests, Profile, Userstats

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Userstats)
class UserstatsAdmin(admin.ModelAdmin):
    pass