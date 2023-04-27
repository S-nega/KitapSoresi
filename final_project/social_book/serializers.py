from django.utils.datetime_safe import datetime
from rest_framework import serializers
from social_book.models import *
from datetime import datetime


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.HiddenField(default=datetime.now)
    no_of_likes = serializers.HiddenField(default=0)
    class Meta:
        model = Post
        fields = "__all__"

#
# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = Profile
#         fields = "__all__"
#
class ProfileSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    id_user = serializers.IntegerField()
    bio = serializers.CharField(read_only=True)
    number = serializers.CharField(read_only=True)
    profileimg = serializers.ImageField(read_only=True)
    location = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        username = validated_data["username"]
        user = get_user_model().objects.get(username=username)
        instance.user = user
        instance.id_user = validated_data.get("id_user", instance.id_user)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.number = validated_data.get("number", instance.number)
        instance.profileimg = validated_data.get("profileimg", instance.profileimg)
        instance.location = validated_data.get("location", instance.location)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = "__all__"


class FollowersCountSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = FollowersCount
        fields = "__all__"


class LikePostSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = LikePost
        fields = "__all__"
