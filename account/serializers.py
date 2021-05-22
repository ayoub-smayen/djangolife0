from rest_framework import serializers 
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Profile
from api.models import User
#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    #image_path = serializers.SerializerMethodField()
    #current_user = serializers.SerializerMethodField('_user')
    #user_id= request.user.id
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    # Use this method for the custom field
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user
    class Meta:
        model = Profile
        fields = ['email','description','image','user']
        extra_kwargs = {
            'image': {
                'write_only' : True,
            }
        }
    
    def get_image_path(self ,obj):
        return obj.image.url

#userInfoSerializer
class GetUserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User 
        fields = ['id','username' ,'email' ,'first_name' ,'last_name','profile']

    def get_profile(self ,obj):
        try :
            profile = obj.profile
            return ProfileSerializer(profile).data
        except :
            return None


class UpdateUserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' ,'email' ,'first_name' ,'last_name','id']

    def validate(self ,data):
        c_user_id = self.context['request'].user.id
        user = User.objects.filter(username = data['username']).exclude(id = c_user_id)
        if user.exists() :
            raise serializers.ValidationError({'error' : 'user with this username already exists'})

        user = User.objects.filter(email = data['email']).exclude(id = c_user_id)
        if user.exists() :
            raise serializers.ValidationError({'error' : 'user with this email already exists'})

        return data

#Profile Update Serializer
class UpdateProfileSer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email','description','image']

class UpdateImageProfileSer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image',]