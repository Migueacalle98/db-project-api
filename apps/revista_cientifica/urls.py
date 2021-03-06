from django.urls import path
from rest_framework import routers

from .viewsets import (UserViewSet, DetailUserViewSet, UpdateUserViewSet, AuthorViewSet,
                       ArticleViewSet, NotificationViewSet, FileViewSet, MCCViewSet,
                       ParticipationViewSet,  RefereeViewSet,
                       ArticleInReviewViewSet, LoginUserViewSet)

router = routers.DefaultRouter()
router.register('author', AuthorViewSet)
router.register('article', ArticleViewSet)
router.register('notification', NotificationViewSet)
router.register('file', FileViewSet)
router.register('mcc', MCCViewSet)
router.register('participation', ParticipationViewSet)
router.register('referee', RefereeViewSet)
router.register('article_in_review', ArticleInReviewViewSet)
router.register('user/update', UpdateUserViewSet, basename='update user')
router.register('user/login', LoginUserViewSet, basename='login user')
router.register('user', UserViewSet, basename='user')
router.register('user', DetailUserViewSet, basename='user')

urlpatterns = (
    router.urls + [
    ]
)
