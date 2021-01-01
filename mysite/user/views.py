from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import collect_blogs, User, email_reminder, feedback
from django.http import HttpResponse
from article.models import Article, Country, University
from django.core.paginator import Paginator
from user.models import email_reminder

'''# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #username, email=None, password=None, **extra_fields
        user = User.objects.create_user(username=username,password=password)
        user.save()
    if user:
        auth.login(request, user)
    return render(request,'register.html')
'''
def register(request):
    refer = request.META.get('HTTP_REFERER', '/')
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'register.html', context={'form': form})

def log_in(request):
    user_name = request.POST.get('username','')
    pass_word = request.POST.get('password','')
    user = authenticate(request, username = user_name, password= pass_word)
    refer = request.META.get('HTTP_REFERER','/')
    if user is not None:
        login(request, user)
        return redirect(refer)
    else:
        return render(request,'error.html',{'message': 'login information does not match'})


def log_out(request):
    logout(request)
    return redirect('/')


def user_center(request):
    if request.user.is_authenticated:
        context={}
        context['email']=request.user.email
        context['name'] = request.user.username
        context['confirmed'] = User.objects.get(id =request.user.pk).confirmed
        context['expire'] = User.objects.get(id =request.user.pk).expire


        return render(request,'user.html',context)
    else:
        return render(request,'error.html',{'message': 'Please log in first'})
    pass


def collect(request):
    blog_id = request.POST.get('blog_id', 0)
    user_id = request.POST.get('user_id', 0)
    print('got post', blog_id,user_id)
    #fav_type = request.POST.get('fav_type', 0)

    if not request.user.is_authenticated:
        # 判断用户登录状态
        return HttpResponse('{"status":"fail", "msg":"not_logged"}', content_type='application/json')
    else:

        if collect_blogs.objects.filter(user_id=user_id, library_id=int(blog_id)).exists():
            exist_record = collect_blogs.objects.filter(user_id=user_id, library_id=int(blog_id))
            exist_record.delete()
            return HttpResponse('{"status":"fail", "msg":"collection removed"}', content_type='application/json')
        else:
            user_fav = collect_blogs()
            user_fav.user = User.objects.get(id= user_id)
            user_fav.library = Article.objects.get(pk= blog_id)
            user_fav.save()
            return HttpResponse('{"status":"success", "msg":"Saved"}', content_type='application/json')

def my_jobs(request):
    if request.user.is_authenticated:
        collect_blogs = Article.objects.filter(user_collect__collected_library=request.user.pk)
        blogs_all = collect_blogs
        paginator = Paginator(blogs_all, 10)
        page_num = request.GET.get('page', 1)
        blog_page = paginator.get_page(page_num)

        context = {}
        context['blogs'] = blog_page
        context['heading'] = 'Saved Jobs'

        return render(request, 'base_backup.html', context)
    else:
        return render(request, 'register.html')

def my_sub(request):
    if request.user.is_authenticated:
        context = {}
        context['country_list'] = Country.objects.all().order_by('country')
        context['university_list'] = University.objects.all().order_by('university')
        context['heading'] = 'Edit My Email Alert'
        reminder = email_reminder.objects.filter(user_id = request.user.pk)
        context['sub'] = reminder
        context['confirmed'] = User.objects.get(id= request.user.pk).confirmed


        return render(request, 'subscription.html', context)
    else:
        return render(request, 'register.html')

def del_sub(request):
    sub_id = request.POST.get('sub_id', 0)
    user_id = request.POST.get('user_id', 0)
    print('got post', sub_id ,user_id)

    if not request.user.is_authenticated:
        # 判断用户登录状态
        return HttpResponse('{"status":"fail", "msg":"not_logged"}', content_type='application/json')
    else:

        if email_reminder.objects.filter(user_id=user_id, id=int(sub_id)).exists():
            exist_record = email_reminder.objects.filter(user_id=user_id, id=int(sub_id))
            exist_record.delete()
            return HttpResponse('{"status":"success", "msg":"collection removed"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"subscription not found"}', content_type='application/json')


def cre_sub(request):
    user_id = request.POST.get('user_id', 0)
    new_sub = email_reminder()
    new_sub.user = User.objects.get(id=user_id)
    new_sub.key_word = request.POST.get('keywords', 0)

    try:
        country_value = request.POST.get('country',0).split(',') # sometimes country could be empty (none selected)
        try:
            new_sub.country_1 = Country.objects.get(country=country_value[0]) #sometimes country number is less than 5
            new_sub.country_2 = Country.objects.get(country=country_value[1])
            new_sub.country_3 = Country.objects.get(country=country_value[2])
            new_sub.country_4 = Country.objects.get(country=country_value[3])
            new_sub.country_5 = Country.objects.get(country=country_value[4])
        except IndexError:
            pass

    except AttributeError:
        pass

    try:
        university_value = request.POST.get('university').split(',')
        try:
            new_sub.university_1 = University.objects.get(university=university_value[0])
            new_sub.university_2 = University.objects.get(university=university_value[1])
            new_sub.university_3 = University.objects.get(university=university_value[2])
            new_sub.university_4 = University.objects.get(university=university_value[3])
            new_sub.university_5 = University.objects.get(university=university_value[4])
        except IndexError:
            pass

    except AttributeError:
        pass

    new_sub.frequency = request.POST.get('fre')
    new_sub.save()
    return HttpResponse('ok', content_type='application/json')

def add_feedback(request):
    new_feedback = feedback()
    new_feedback.user = User.objects.get(id = request.POST.get('user_id', 0))
    new_feedback.comments = request.POST.get('feedback', 0)
    new_feedback.new_url = request.POST.get('url', 0)
    new_feedback.save()
    return HttpResponse('We have received your message, thanks!', content_type='application/json')