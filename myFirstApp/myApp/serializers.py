from rest_framework import serializers
#   from myApp.models import Post
from myApp.models import *
class ExclusiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exclusive
        exclude = []

class BestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Best
        exclude = []

class LatestBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = LatestBlog
        exclude = []