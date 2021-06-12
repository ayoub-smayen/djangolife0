

from api.serializers import UserSerializer

from .models import Feed, FeedLike, FeedComment
from rest_framework import  serializers
class FeedCommentSer(serializers.ModelSerializer):
    #owner = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta():
        model = FeedComment
        fields = '__all__'
        read_only_fields = ['owner' ,'u_date' ,'p_date']

    def get_owner(self ,obj):
        return UserSerializer(obj.owner).data


class FeedLikeCommentUpdateSer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta():
        model = FeedComment
        fields = '__all__'
        read_only_fields = ['feed', 'owner', 'u_date', 'p_date']

    def get_owner(self, obj):
        request = self.context.get('request', None)
        if request:
            print(request.user)
            return request.user.id
        #return UserSerializer(obj.owner).data


# like serializer
class FeedLikeSer(serializers.ModelSerializer):
    class Meta():
        model = FeedLike
        fields = '__all__'
        read_only_fields = ['owner', ]

    def validate(self, data):
        owner_id = self.context['request'].user.id
        feed = data['feed']

        like = FeedLike.objects.filter(owner=owner_id, feed=feed.id)
        if like.exists():
            raise serializers.ValidationError("this like with this user and post already exists")
        return data


# like Update serializer
class FeedLikeUpdateSer(serializers.ModelSerializer):
    class Meta():
        model = FeedLike
        fields = '__all__'
        read_only_fields = ['owner', 'feed']



class FeedSer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #owner = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    delikes_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta():
        model = Feed
        fields = '__all__'

    def get_owner(self ,obj):
        request = self.context.get('request', None)
        if request:
            print(request.user)
            return request.user.id
        #return UserSerializer(obj.owner).data

    def get_comments_count(self ,obj):
        return obj.feedcomments.count()

    def get_likes_count(self ,obj):
        return obj.feedlikes.filter(like = True).count()

    def get_delikes_count(self ,obj):
        return obj.feedlikes.filter(like = False).count()

    def get_likes(self,obj):
        return FeedLikeSer(obj.feedlikes ,many = True).data