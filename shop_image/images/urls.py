from django.urls import path

# Import the views
from .views import upload, delete, update, search, download_image


app_name = "images"

urlpatterns = [
    path('upload/', upload, name='upload'),
    path("delete/<int:pk>/", delete, name="delete"),
    path('update/<int:pk>/', update, name="update"),
    path("search/", search, name="search"),
    path('download/<int:pk>/', download_image, name="download_image")
]
