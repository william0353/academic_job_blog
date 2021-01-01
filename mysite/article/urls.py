from django.urls import path
from . import views, api_views

urlpatterns = [
    path('<int:article_id>',views.blog_detail, name='blog_detail'),
    path('v1/post',api_views.api_post, name='update'),
    path('v1/test',api_views.test, name='test'),

]