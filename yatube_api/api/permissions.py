from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка прав на чтение или авторство постов."""
    message = "Изменение или удаление чужого контента запрещено!"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
