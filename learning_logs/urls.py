"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    # 指定Topic的详情页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 指定"添加新主题"的页面url模式
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 指定"添加新条目"的页面url模式
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 编辑条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # 编辑主题
    url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
]






