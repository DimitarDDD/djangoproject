"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from posts.views import posts_list,post_detail, post_add, search_posts, edit_post, like_post, unlike_post, follow_person, unfollow_person 
from django.views.static import serve
from django.conf import settings
from accounts.views import register  
from django.urls import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'), 
    path('accounts/password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('accounts/password-reset/done/', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('accounts/password-reset/complete/', password_reset_complete, name='password_reset_complete'),
    path( '',posts_list, name="home"),
    path( '',posts_list, name="posts_list"),  
    path('posts/<int:id>',post_detail, name="post_detail"),  
    path('posts/<int:id>/edit',edit_post , name="edit_post"), 
    path('post/add',post_add,  name='post_add'), 
    path('search', search_posts, name='search_posts'), 
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}), 
    path('like_post/<int:id>', like_post, name="like_post"),
    path('unlike_post/<int:id>', unlike_post, name="unlike_post"), 
    path('follow_person/<int:id>', follow_person, name="follow_person"),
    path('unfollow_person/<int:id>', unfollow_person, name="unfollow_person"),

]
