from django.contrib import admin
from .models import Article, Region,Country,University,Discipline,Types, add_source
from user.models import email_reminder, User
from user import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','university','country','discipline','types','create_time')


'''class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name')'''

admin.site.register(add_source)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(University)
admin.site.register(Discipline)
admin.site.register(Types)
#admin.site.register(models.CustomUser, UserAdmin)
admin.site.register(User)
admin.site.register(email_reminder)


