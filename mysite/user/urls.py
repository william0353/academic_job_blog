from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('log-out/',views.log_out, name='log-out'),
    path('center/', views.user_center, name ='user-center'),
    path('collect/', views.collect, name ='collect_blogs'),
    path('my-jobs/', views.my_jobs, name ='my_jobs'),
    path('my-subscriptions/', views.my_sub, name ='my_subscriptions'),
    path('del-sub/', views.del_sub, name ='del_sub'),
    path('cre-sub/', views.cre_sub, name ='cre_sub'),
    path('feedback/', views.add_feedback, name ='feedback'),
]