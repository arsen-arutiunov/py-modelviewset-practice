from django.urls import path

from author.views import AuthorViewSet

urlpatterns = [
    path("manage/", AuthorViewSet.as_view({"get": "list", "post": "create"}),
         name="manage-list"),
    path("manage/<int:pk>/", AuthorViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }), name="manage-detail"),
]

app_name = "author"
