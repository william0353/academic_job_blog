from django.db import models
#import user.User

# Create your models here.


class Region(models.Model):
    #content_list = ['Asia', 'South America', 'North America', 'Europe', 'Oceania', 'Africa']
    content = models.CharField(max_length=10)

    def __str__(self):
        return self.content


class Country(models.Model):
    country = models.CharField(max_length=15)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True)



    def __str__(self):
        return self.country


class University(models.Model):
    university = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.university

    @property
    def search_by_country(self):
        return self.all()

class Discipline(models.Model):
    discipline = models.CharField(max_length=20)

    def __str__(self):
        return self.discipline

class Types(models.Model):
    types = models.CharField(max_length=20)

    def __str__(self):
        return self.types

class Article(models.Model):
    title = models.CharField(max_length=150)
    context = models.TextField()
    url = models.URLField()
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    types = models.ForeignKey(Types, on_delete=models.DO_NOTHING)
    create_time =models.DateField(auto_now= True)
    create_time_roll = models.DateTimeField(auto_now=True)
    user_collect = models.ManyToManyField('user.User', through='user.collect_blogs')

    # add available user_group

    def __str__(self):
        return "<Article:%s>" % self.title

    class Meta:
        ordering =['-create_time_roll']


class add_source(models.Model):
    url = models.URLField(null=True)
    universty = models.ForeignKey(University,on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING,null=True,blank=True)
    list_id = models.CharField(max_length=200,null=True,blank=True)
    list_class = models.CharField(max_length=200,null=True,blank=True)
    title_id = models.CharField(max_length=200, null=True, blank=True)
    title_class = models.CharField(max_length=200, null=True, blank=True)
    body_id = models.CharField(max_length=200, null=True, blank=True)
    body_class = models.CharField(max_length=200, null=True, blank=True)



