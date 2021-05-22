from rest_framework import serializers
from .models import  UserProfile
# from   userprofile.serializers import  *

#from userprofile.models import *
#from django.contrib.auth.models import  User
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only': True},}
    def create(self, validated_data):
        #user = User.objects.create_user(username=validated_data['username'], email =validated_data['email'],     password = validated_data['password'])

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        #user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields =('title', 'dob', 'address', 'country', 'city', 'zip', 'photo',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # userprofile = UserProfileSerializer(required=True)
    # friends = serializers.SerializerMethodField()
    # user_recipes = serializers.SerializerMethodField()
    # friends_recipes = serializers.SerializerMethodField()
    # favorites = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'userprofile',
                  #'friends','user_recipes','friends_recipes','favorites',

                  )
        extra_kwargs = {'password': {'write_only': True}}

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
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

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