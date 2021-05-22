from django.contrib.auth import update_session_auth_hash

from cart0.permissions import  IsOwnerOrReadOnly , IsStaffOrTargetUser
from  rest_framework import  serializers

from .models import  Myprofile
#from django.contrib.auth.models import User
from api.models import User
class MyprofileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Myprofile
        fields = ('id','first_name','last_name','user','gender','zip_code','image_pic',)



    def get_username(self, obj):
        obj.user = self.request.user.id
        return obj.user.username



    def create(self, validated_data):
        return Myprofile.objects.create(**validated_data)



class UserSerializer(serializers.ModelSerializer):
    myprofile = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'myprofile')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }



    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        instance.owner = validated_data.pop('owner')
        # Update User data
        instance.user = validated_data.get('user',instance.user)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('first_name', instance.email)
        # Update UserProfile data
        if not instance.profile:
            Myprofile.objects.create(user=instance, **profile_data)
        instance.profile.zip_code= profile_data.get('zip_code', instance.profile.zip_code)
        instance.profile.gender = profile_data.get('gender', instance.profile.phone)
        instance.profile.image_pic = profile_data.get('imahe_pic', instance.profile.image_pic)
        instance.save()
        # Check if the password has changed
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
            update_session_auth_hash(self.context.get('request'), instance)

        return instance