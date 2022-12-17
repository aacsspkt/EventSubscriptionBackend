from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsNotAuthenticated(BasePermission):
    """Permit only users that are NOT logged in!"""
    def has_permission(self, request, view):
        return request.user.is_anonymous


class IsAdminOrReadOnly(BasePermission):
    """
    Ensures user is staff when creating or updating an user otherwise return a
    HTTP forbidden (403)
    """
    def has_permission(self, request, view):
        # safe methods are get, head, options
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_staff



class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        #check request method whether this is only to reterive or other
        #if for only reading (safe), then ok
        if request.method in permissions.SAFE_METHODS:
            return True

        #otherwise, check user is same as the person object that he is trying to update,etc
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id