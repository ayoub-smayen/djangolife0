from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User
from api.models import  User
from .models import Feed
from .serializers import FeedSer
from .custom_permissions import isOwnerOrReadOnly
from rest_framework import filters
from rest_framework import pagination

from .pagination import MyPagination
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import pagination
from rest_framework import filters

from .models import FeedComment,FeedLike
from .serializers import   FeedLikeCommentUpdateSer, FeedSer,FeedLikeSer ,FeedLikeUpdateSer, FeedCommentSer
from  .custom_permissions import isOwnerOrReadOnly
from .models import Feed
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly ,
        isOwnerOrReadOnly,
    ]
    pagination_class = MyPagination
    filter_backends = [filters.OrderingFilter]
    ordering = ['-p_date']

    def perform_create(self ,serializer):
        serializer.save(owner = self.request.user)

    @action(detail = True)
    def get_user_posts(self , request ,pk = None):
        owner = get_object_or_404(User , pk = pk)
        owner_posts = Feed.objects.filter(owner = owner.id)
        serializer = FeedSer(owner_posts , many = True)
        return Response(serializer.data)


#from django.shortcuts import get_object_or_404

#from .serializers import PostSer


class FeedCommentViewSet(viewsets.ModelViewSet):
    queryset = FeedComment.objects.all()
    serializer_class = FeedCommentSer
    permission_classes = [
        permissions.IsAuthenticated,
        isOwnerOrReadOnly,
    ]
    filter_backends = [filters.OrderingFilter]
    ordering = ['-p_date']

    def perform_create(self ,serializer):
        return serializer.save(owner = self.request.user)

    def update(self ,request , pk=None):
        comment = get_object_or_404(FeedComment ,id = pk)
        self.check_object_permissions(request , comment)
        serializer = FeedLikeCommentUpdateSer(comment ,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comment = serializer.data
        return Response(comment)

    @action(detail=True)
    def get_comments(self ,request ,pk = None):
        post = get_object_or_404(Feed ,pk = pk)
        feedcomment = FeedComment.objects.filter(post = post).order_by('-p_date')
        return Response( FeedLikeSer(feedcomment ,many = True).data )

class FeedLikeViewSet(viewsets.ModelViewSet):
    queryset = FeedLike.objects.all()
    serializer_class = FeedLikeSer
    permission_classes = [
        permissions.IsAuthenticated,
        isOwnerOrReadOnly,
    ]

    def perform_create(self ,serializer):
        return serializer.save(owner = self.request.user)

    def create(self ,request , pk=None):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner = self.request.user)
        feed_id = serializer.data["feed"]
        feed = Feed.objects.get(id = feed_id)
        return Response(FeedSer(feed).data)

    def update(self ,request , pk=None):
        like = get_object_or_404(FeedLike ,id = pk)
        feed = like.feed
        self.check_object_permissions(request , like)
        serializer = FeedLikeUpdateSer(like ,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(FeedSer(feed).data)

    def destroy(self ,request , pk=None):
        like = get_object_or_404(FeedLike ,id = pk)
        feed = like.feed
        self.check_object_permissions(request , like)
        like.delete()
        return Response(FeedSer(feed).data)
