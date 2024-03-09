from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Permission for checking owner"""
    message = "You are not owner"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUser(BasePermission):
    """Permission for checking user"""
    message = "You are not owner"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
