# -*- coding: utf-8 -*-

from rest_framework import serializers
#from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
#:apiview
from django.utils import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer

#: 为用户模型添加端点
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')    

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets', 'owner')

class JsonResponse(Response):
    def __init__(self, data=None, code=None, desc=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super(Response, self).__init__(None, status=status)
        if isinstance(data, serializer):
            msg = (
                  'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
           )
            raise AssertionError(msg)
        self.data = {"code": code, "desc": desc, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value


    def get(self, request, snippet_pk):
        snippet = get_object_or_404(House, pk=snippet_pk) #获取数据
        data = HouseSerializer(house) #序列化
        return api_response.JsonResponse(data=data.data, code=status.HTTP_200_OK, desc='get house success') 

#:使用ModelSerializer类来重写Serializer类

class SnippetSerializer(serializers.ModelSerializer):
   class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'desc', 'status', 'template_name','headers', 'exception', 'content_type')





#: 下面是使用Serializer类
"""
class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    msg = serializers.CharField(required=False, allow_blank=True, max_length=100)
    data = serializers.CharField(required=False, allow_blank=True, max_length=100)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.msg = validated_data.get('msg', instance.msg)
        instance.data = validated_data.get('msg', instance.data)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)

        instance.style = validated_data.get('style', instance.style)

        instance.save()
        return instance

"""


"""
#from rest_framework import serializers
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineos = serialziers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        #: 创建并返回一个新的Snippet实例，得到合法的数据
        return Snippets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #: 更新并返回一个已经存在的'Snippet'实例，同时获取合法的数据
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.lineos = validated_data.get('lineos', instance.lineos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""
