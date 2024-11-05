from django.urls import path, include
from rest_framework import routers


from author.views import AuthorViewSet


router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="author-list")

author_list = AuthorViewSet.as_view(
    actions={"get": "list",
             "post": "create"}
)

author_detail = AuthorViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy"}
)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "author"
