from rest_framework import permissions

class IsSimpleUser(permissions.BasePermission):
    def has_permission(self, request, view):        
        if request.user.groups.filter(name='USER'):
            return True
        return False


class IsFastChecker(permissions.BasePermission):
    def has_permission(self, request, view):        
        if request.user.groups.filter(name='FASTCHECKER'):
            return True
        return False