


from rest_framework import serializers
from .models import  Poststory , PostImage
from api.models import User





class PoststorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #comment  =CommentSerializer(many=True,read_only=True)
    # comment = serializers.SerializerMethodField()
    #
    # def get_comments(self, obj):
    #     queryset = Comments.objects.filter(post_id=obj.id,)
    #     serializer = CommentSerializer(queryset, many=True)
    #     return serializer.data

    # comments = serializers.SerializerMethodField()
    # def get_comment(self, obj):
    #     try:
    #         friend = Comments.objects.get(current_user=obj)
    #         friends = friend.users.all()
    #     except:
    #         friends = None
    #         return []
    #     friends_serializer = CommentSerializer(friends, many=True)
    #     return friends_serializer.data
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            print(request.user)
            return request.user.id
    class Meta:
        model = Poststory
        fields = ('__all__')


class PostImageSerializer(serializers.ModelSerializer):
    #post = PoststorySerializer(many=True,read_only=True)

    class Meta:
        model = PostImage
        fields = ("__all__")

class UserSerializer(serializers.ModelSerializer):
    #comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    poststory  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','poststory',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }