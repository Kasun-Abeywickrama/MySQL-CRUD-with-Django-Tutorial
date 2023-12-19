# urls.py
from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDeleteView

urlpatterns = [
    # URL patterns for the CRUD views
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view(), name='student-retrieve-update-delete'),
]
