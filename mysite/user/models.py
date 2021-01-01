from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta



class User(User):
    c_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    pay_time = models.DateTimeField(null=True, blank=True, default=None)
    expire = models.DateField(null=True,blank=True,default=None)

    @property
    def make_pay(self):
        pay_time = datetime.datetime.now()
        expire = self.pay_time + relativedelta(years=1)

        return None
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'

'''    @property
    def expire_date(self):
        if self.pay_time is not None:
            expire =self.pay_time + relativedelta(years=1)
            return expire
        else:
            return None'''




class key_word(models.Model):
    word = models.CharField(max_length=50)
    creater = models.ManyToManyField(User)


class email_reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_reminder', verbose_name='users')
    key_word = models.CharField(max_length=200, null=True)
    discipline = models.ForeignKey('article.Discipline',related_name='discipline_choice',null=True, blank=True, on_delete=models.CASCADE)
    country_1 =models.ForeignKey('article.Country',related_name='country_1', null=True, blank=True, on_delete=models.CASCADE)
    country_2 = models.ForeignKey('article.Country',related_name='country_2',null=True,blank=True, on_delete=models.CASCADE)
    country_3 = models.ForeignKey('article.Country',related_name='country_3',null=True,blank=True, on_delete=models.CASCADE)
    country_4 = models.ForeignKey('article.Country',related_name='country_4',null=True,blank=True, on_delete=models.CASCADE)
    country_5 = models.ForeignKey('article.Country',related_name='country_5',null=True,blank=True, on_delete=models.CASCADE)

    university_1 = models.ForeignKey('article.University',related_name='university_1',null=True,blank=True, on_delete=models.CASCADE)
    university_2 = models.ForeignKey('article.University',related_name='university_2',null=True,blank=True, on_delete=models.CASCADE)
    university_3 = models.ForeignKey('article.University',related_name='university_3',null=True,blank=True, on_delete=models.CASCADE)
    university_4 = models.ForeignKey('article.University',related_name='university_4',null=True,blank=True, on_delete=models.CASCADE)
    university_5 = models.ForeignKey('article.University',related_name='university_5',null=True,blank=True, on_delete=models.CASCADE)

    frequent_choice=[('per month','Per Month'),('per week','Per Week'),('per day','Per Day'),('immediately','Fastest'),('wrong','wrong reminder')]
    frequency = models.CharField(max_length=15, choices=frequent_choice, default='per month')


    def __str__(self):
        return self.frequency



class collect_blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collected_library', verbose_name='users')
    library = models.ForeignKey('article.Article', on_delete=models.CASCADE, related_name='user_collected_library',
                                verbose_name='library')

    def __str__(self):
        return self.library.name

class feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    comments = models.CharField(max_length=500,null=True,blank=True)
    new_url = models.CharField(max_length=500, null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
