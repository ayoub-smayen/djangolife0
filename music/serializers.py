
from rest_framework import serializers
from .models import Song, Album
#from django.contrib.auth.models import User
from  api.models import  User
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("__all__")
            #[ 'album_id','song_title', 'audio_file','is_favorite']

class AlbumSerializer(serializers.ModelSerializer):
    songs = TrackSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            print(request.user)
            return request.user.id

    class Meta:
        model = Album
        fields = ('__all__')
            #['id','author','album_logo','album_title', 'artist', 'is_favorite','genre','songs']
    def get_username(self, obj):
        obj.author = self.request.user.id
        return obj.author.username



class UserSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'album')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }