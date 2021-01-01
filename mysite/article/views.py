from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Article, Region, Country, University,Discipline, Types
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
from django.db.models import Q



# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):

    blogs_all = Article.objects.all()
    paginator = Paginator(blogs_all,10)
    page_num = request.GET.get('page', 1)
    blog_page = paginator.get_page(page_num)

    context ={}
    context['blogs'] = blog_page
    #context['content'] = mark_safe(Article.objects.all().context)
    return  render(request,'base_backup.html',context)


def blog_detail(request,article_id):
    context ={}
    blog = get_object_or_404(Article, id= article_id)
    context['blogs']=blog
    context['title']=blog.title
    context['content'] = mark_safe(blog.context)
    context['previous'] = Article.objects.filter(create_time_roll__gt =blog.create_time_roll).last()
    context['next'] = Article.objects.filter(create_time_roll__lt=blog.create_time_roll).first()
    #context['url'] = get_object_or_404(Article.url, id= article_id)
    return render(request,'blog_detail_backup.html',context)

def type_list(request):
    context = {}
    #blog_type = get_object_or_404(Types, pk= types_pk)
    #context['blog_type'] = blog_type
    #context['blogs'] = Article.objects.filter(types= blog_type)
    context['blog_types'] = Types.objects.all()
    context['blog_countries'] = Country.objects.all()
    context['blog_regions'] = Region.objects.all()
    context['blog_uni'] = University.objects.all()
    context['blog_disc'] = Discipline.objects.all()
    return render(request,'label_list.html',context)

def deep_search(request):
    context = {}
    # blog_type = get_object_or_404(Types, pk= types_pk)
    # context['blog_type'] = blog_type
    # context['blogs'] = Article.objects.filter(types= blog_type)
    context['blog_types'] = Types.objects.all()
    context['blog_countries'] = Country.objects.all()
    context['blog_regions'] = Region.objects.all()
    context['blog_uni'] = University.objects.all()
    context['blog_disc'] = Discipline.objects.all()
    return render(request,'deep_search.html', context)

def search_context(request):
    raw_string = request.GET.get('key_words', 'Notfound')
    print(str(raw_string))
    context = {}

    if str(raw_string) !='Notfound':
        if ' ' in str(raw_string):
            print('yessss')
            key_words = str(raw_string).split()
            #results = Article.objects.all()
            for words in key_words:
                results = Article.objects.filter(context__icontains = words)


        else:
            results = Article.objects.filter(context__icontains = raw_string)

    else:
        results = Article.objects.all()
    paginator = Paginator(results, 10)
    page_num = request.GET.get('page', 1)
    blog_page = paginator.get_page(page_num)
    context['blogs'] = blog_page

    return render(request,'base_backup.html',context)




#Note 反向查询gG foreign-key__origin-name=... see line 51,65,78
def vacancies_view(request):
    types = request.GET.get('type',1)
    blogs_all = Article.objects.filter(types__types=types)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all, 10)
    blog_page = paginator.get_page(page_num)
    context = {}
    context['blogs'] = blog_page
    context['heading'] = str(types)
    # context['content'] = mark_safe(Article.objects.all().context)
    return render(request, 'base_backup.html', context)


def country_view(request):
    types = request.GET.get('type', 1)
    blogs_all = Article.objects.filter(country__country=types)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all, 10)
    blog_page = paginator.get_page(page_num)
    context = {}
    context['blogs'] = blog_page
    context['heading'] = str(types)
    # context['content'] = mark_safe(Article.objects.all().context)
    return render(request, 'base_backup.html', context)

def dis_view(request):
    types = request.GET.get('type', 1)
    blogs_all = Article.objects.filter(discipline__discipline=types)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all, 10)
    blog_page = paginator.get_page(page_num)
    context = {}
    context['blogs'] = blog_page
    context['heading'] = str(types)
    # context['content'] = mark_safe(Article.objects.all().context)
    return render(request, 'base_backup.html', context)

def rig_view(request):
    types = request.GET.get('type', 1)
    blogs_all = Article.objects.filter(region__content=types)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all, 10)
    blog_page = paginator.get_page(page_num)
    context = {}
    context['blogs'] = blog_page
    context['heading'] = str(types)
    # context['content'] = mark_safe(Article.objects.all().context)
    return render(request, 'base_backup.html', context)

def ist_view(request):
    types = request.GET.get('type', 1)
    blogs_all = Article.objects.filter(university__university=types)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all, 10)
    blog_page = paginator.get_page(page_num)
    context = {}
    context['blogs'] = blog_page
    context['heading'] = str(types)
    # context['content'] = mark_safe(Article.objects.all().context)
    return render(request, 'base_backup.html', context)