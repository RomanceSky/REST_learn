from django.db import models

# Create your models here.
"""
__________________________________________

时间: 2018-04-07
作者: Jun
设计博客的数据库表结构
博客最主要的功能是展示文章
博客文章:
   标题、正文、作者、发表时间、分类、标签、热门文章、最新文章
用户
   姓名、联系方式
用户操作
   点赞、喜欢、分享、评论、收藏
用户登录
参考:https://foofish.net
关于
RSS订阅
__________________________________________

"""

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

#: 用pygments代码高亮库来形成高亮字段,添加额外的引用
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
#    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    msg = models.CharField(max_length=100, blank=True, default='')
    data = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=100, blank=True, default='')
    template_name = models.CharField(max_length=100, blank=True, default='')
    exception = models.CharField(max_length=100, blank=True, default='')
    content_type = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    headers = models.CharField(max_length=100, blank=True, default='')

    #:认证和权限
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='snippets')

    highlighted = models.TextField()


   
    class Meta:
        ordering = ('created',)

#: 认证和权限，为模型类添加.save()方法
    def save(self, *args, **kwars):
        """
        Use the 'pygments' library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self,language)
        lineos = slef.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, lineos=lineos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)















