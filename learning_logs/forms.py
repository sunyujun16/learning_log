from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """empty"""
    class Meta:
        model = Topic
        fields = ['text', 'public']
        labels = {'text': '', 'public': '设为公开'}


class Entry_form(forms.ModelForm):
    """通过获取entry模型来定制表单的属性, 该类的实例被django用来自动生成表单以及将Meta内的变量关联到数据库的Entry属性等"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


