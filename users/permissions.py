from rest_framework import permissions


class AdsPermissions(permissions.BasePermission):
    """
    Доступы для объявлений
    - list: доступно анонимному пользователю
    - retrieve/create: доступно аутентифицированным пользователям
    - update/destroy: доступно автору объявления или администратору
    """

    def has_permission(self, request, view):
        if view.action == "list":
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        return view.action in (
            "retrieve",
            "create",
            "update",
            "partial_update",
            "destroy",
        )

    def has_object_permission(self, request, view, obj):
        if getattr(request.user, "role", None) == "admin":
            return True
        if getattr(obj, "author", None) == request.user:
            return view.action in (
                "retrieve",
                "update",
                "partial_update",
                "destroy",
            )
        if view.action == "retrieve":
            return request.user and request.user.is_authenticated
        return False


class ReviewPermissions(permissions.BasePermission):
    """
    Доступы для отзывов
    - список комментариев: доступно только аутентифицированным пользователям
    - создание комментария: аутентифицированный пользователь
    - редактирование/удаление: только автор или админ
    - просмотр одного комментария: доступно аутентифицированному пользователю
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return view.action in (
            "list",
            "retrieve",
            "create",
            "update",
            "partial_update",
            "destroy",
        )

    def has_object_permission(self, request, view, obj):
        if getattr(request.user, "role", None) == "admin":
            return True
        if view.action in ("retrieve", "list", "create"):
            return True
        if getattr(obj, "author", None) == request.user:
            return view.action in ("update", "partial_update", "destroy")
        return False
