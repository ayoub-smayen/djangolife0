from rest_framework import serializers
from .models import RecipeVideo
# from django.contrib.auth.models import User
from api.models import User
from core.serializers import UserSerializerWithToken


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    # class Meta:
    # model = Recipe
    # fields = '__all__'
    # username = serializers.RelatedField(read_only=True)
    # author = serializers.HiddenField(
    # default=serializers.CurrentUserDefault())
    # serializers.SerializerMethodField()
    # author = serializers.RelatedField(read_only=True)
    # u = UserSerializerWithToken()"_user"
    # username =  context.get("request").user
    # def  getCurrentUser(request):
    # username =u.get_token(self.request.user)
    # return username
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            print(request.user)
            return request.user.id

    # username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = RecipeVideo
        fields = [
            'id',
            'title',
            'author',
            #'video',
            'cooktime',
            'ingredients',
            'created_date',
            'directions',
            'picture',
            'video'


        ]

    def get_username(self, obj):
        obj.author = self.request.user.id
        return obj.author.username


class UserSerializer(serializers.ModelSerializer):
    reciepsvideo = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'reciepesvideo')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }