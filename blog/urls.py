"""dxflearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from blog import views

app_name = "blog"  # 指定app_name用户反向生成url

# URL 最好是以^开头, 以$结尾, 新版django如果URL中包含正则那么需要引入re_path
urlpatterns = [
    re_path(r'^(?P<version>[v1|v2]+)/articles/$', views.ArticleList.as_view(), name="article-list"),
    re_path(r'^(?P<version>[v1|v2]+)/articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view(), name="article-detail"),
    re_path(r'^(?P<version>[v1|v2]+)/user-article/$', views.UserArticleList.as_view(), name="user-article-list"),
    re_path(r'^(?P<version>[v1|v2]+)/user-article/(?P<pk>[0-9]+)/$',
            views.UserArticleDetail.as_view(), name="user-article-detail"),
    re_path(r'^(?P<version>[v1|v2]+)/async-articles/$', views.AsyncArticleList.as_view(), name="async-article-list"),
    re_path(r'^(?P<version>[v1|v2]+)/async-add/$', views.AddView.as_view(), name="add"),
    re_path(r'^(?P<version>[v1|v2]+)/remove-task/$', views.RemoveTask.as_view(), name="remove-add"),
    re_path(r'^(?P<version>[v1|v2]+)/terminate-task/$', views.TerminateTask.as_view(), name="terminate-add"),
    re_path(r'^(?P<version>[v1|v2]+)/debug-task/$', views.DebugView.as_view(), name="debug-add"),

]
