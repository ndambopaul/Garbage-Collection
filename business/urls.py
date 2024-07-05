from django.urls import path
from business.views import businesses, new_business, edit_business, delete_business

urlpatterns = [
    path("", businesses, name="businesses"),
    path("new-business/", new_business, name="new-business"),
    path("edit-business/", edit_business, name="edit-business"),
    path("delete-business/", delete_business, name="delete-business"),
]