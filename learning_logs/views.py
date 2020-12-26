from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from learning_logs.models import Topic, Entry
from.forms import TopicForm, Entry_form
from django.contrib.auth.decorators import login_required


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


@ login_required
def topics(request):
    """显示所有主题"""
    # topics = []
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # for topic in topic_set:
    #     topics.append(topic)
    context = {'topics': topics}  # topic键值对多写了一个colon, 好家伙找他妈俩小时!!! dear fuck!!!

    return render(request, 'learning_logs/topics.html', context)


@ login_required
def topic(request, topic_id):
    """显示指定id的单个主题及其条目"""

    # 向数据库查询, 建议先在django shell当中尝试, 以确认无误
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


@ login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据, 创建新表单
        form = TopicForm()
    else:
        # POST提交数据, 对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # reverse反向解析URL

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@ login_required
def new_entry(request, topic_id):
    """通过id获取要添加新条目的主题"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交创建空表单
        form = Entry_form()
    else:
        # 提交, 获取请求中的数据, 存入数据库, 并重定向到topic页面
        form = Entry_form(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic  # 关联到主题
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@ login_required
def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 使用当前entry填充表单
        form = Entry_form(instance=entry)
    else:
        form = Entry_form(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)





