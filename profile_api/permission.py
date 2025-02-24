from rest_framework import permissions

class IsOwnerOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read access to everyone.
    - Authenticated users to create new objects.
    - Only owners to modify or delete objects.
    """

    def has_permission(self, request, view):
        # Allow read access for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write access (POST) to authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read access for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write access only to the owner of the object
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allows user update thier own status"""
    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to update"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id