from django.db import models
"""
——————————————————————————

Django2.0文档模型部分练习
时间:2018-04-06
数据库:Mariadb
具体安装见seg文章
作者:jun

—————————————————————————————————————————————————
"""
#:order_with_respect_to 使得这个对象对给定的字段有顺序，通常是一个外键
class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta: 
        order_with_respect_to = 'question'


