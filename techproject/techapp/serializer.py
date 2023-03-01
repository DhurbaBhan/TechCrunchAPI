from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    author=serializers.SerializerMethodField(method_name="get_author")
    category=serializers.SerializerMethodField(method_name="get_category")
    # comment_text=serializers.SerializerMethodField(method_name="get_comment")
    class Meta:
        model=Post
        fields=["image","comment_text","title","body","post_date","category","author","slug"]


    def get_author(self,p:Post):
        return p.author.name  

    def get_category(self,p:Post):
        return p.category.name      

    # def get_comment(self,p:Post):
            # return p.comment_text 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"  

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__" 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"        