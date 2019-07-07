from django.urls import path
from courses.views import (
    my_fbv, CourseView, CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
