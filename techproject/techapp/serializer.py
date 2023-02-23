from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    
    author=serializers.SerializerMethodField(method_name="get_author")
    category=serializers.SerializerMethodField(method_name="get_category")
    comment_text=serializers.SerializerMethodField(method_name="get_comment")
    class Meta:
        model=Post
        fields="__all__"


    def get_author(self,p:Post):
        return p.author.name  

    def get_category(self,p:Post):
        return p.category.name      

    def get_comment(self,p:Post):
        return p.comment_text    