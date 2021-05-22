from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
#from django.contrib.auth.models import User
from api.models import UserProfile,User

# from   userprofile.serializers import  *
#
# from userprofile.models import *
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username',)
#
#
# class UserSerializerWithToken(serializers.ModelSerializer):
#
#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)
#
#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password')




class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ('title', 'dob', 'address', 'country', 'city', 'zip', 'photo','user',)
#ModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer(required=True)

    # friends = serializers.SerializerMethodField()
    # user_recipes = serializers.SerializerMethodField()
    # friends_recipes = serializers.SerializerMethodField()
    # favorites = serializers.SerializerMethodField()
    #userprofile= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url','username','email','first_name', 'last_name', 'password', 'userprofile',)
            # 'friends',
            # 'user_recipes',
            # 'friends_recipes',
            # 'favorites',)

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile')
        profile0 = instance.userprofile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile0.title = profile_data.get('title', profile0.title)
        profile0.dob = profile_data.get('dob', profile0.dob)
        profile0.address = profile_data.get('address', profile0.address)
        profile0.country = profile_data.get('country', profile0.country)
        profile0.city = profile_data.get('city', profile0.city)
        profile0.zip = profile_data.get('zip', profile0.zip)
        profile0.photo = profile_data.get('photo', profile0.photo)
        profile0.save()

        return instance

    # def get_friends(self, obj):
    #     try:
    #         friend = Friend.objects.get(current_user=obj)
    #         friends = friend.users.all()
    #     except:
    #         friends = None
    #         return []
    #     friends_serializer = FriendSerializer(friends, many=True)
    #     return friends_serializer.data
    #
    # def get_user_recipes(self, obj):
    #     my_recipes = Recipe.objects.filter(author=obj.id).order_by(Lower('title'))
    #     recipe_serializer = RecipeSerializer(my_recipes, many=True)
    #     return recipe_serializer.data
    #
    # def get_friends_recipes(self, obj):
    #     try:
    #         friend = Friend.objects.get(current_user=obj)
    #         friends = friend.users.all()
    #     except:
    #         friends = None
    #         return []
    #     friends_recipes = Recipe.objects.filter(author__in=friends).order_by('published_date')
    #     recipe_serializer = RecipeSerializer(friends_recipes, many=True)
    #     return recipe_serializer.data
    #
    # def get_favorites(self, obj):
    #     user_favorites, created = Favorite.objects.get_or_create(user=obj)
    #     favorite_recipes = obj.favorites.favorites.all()
    #     recipe_serializer = RecipeSerializer(favorite_recipes, many=True)
    #     return recipe_serializer.data


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password','email',)