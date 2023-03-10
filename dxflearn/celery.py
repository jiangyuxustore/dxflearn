# -*- coding: utf-8 -*-
"""
@Auth ： 江宇旭
@Email ：jiang.yuxu@mech-mind.net
@Time ： 2023/3/1 16:41
"""
import os
from celery import Celery
from user import tasks as user_task
from steelplate import tasks as steel_task
from blog import tasks as blog_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dxflearn.settings")
app = Celery("django_celery")
# 这个的namespace大写, 那就意味着在django的settings.py中有关celery的配置都要大写
app.config_from_object("django.conf:settings", namespace="CELERY")
# 要使 app.autodiscover_tasks() 自动加载celery任务, 需要在 Django 的每个应用程序内的单独创建
# tasks.py 模块, 并在tasks.py中中定义 Celery 任务
app.autodiscover_tasks()  # 会自动从django的INSTALLED_APPS中的应用目录下加载tasks.py
app.register_task(user_task.UserOperator())  # class base task 需要注册到celery中
app.register_task(steel_task.SteelOriginalInfoOperator())
app.register_task(blog_task.ArticleOperator())
app.register_task(blog_task.ClassBaseAdd())
