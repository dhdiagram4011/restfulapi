from rest_framework import permissions

class IsOnwerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.subscriber == request.user or request.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.subscriber == request.user or request.is_superuser